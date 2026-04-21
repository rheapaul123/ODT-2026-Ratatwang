# ── Imports ─────────────────────────────────────────────
import bluetooth
import time
import math
import random
from machine import Pin, PWM
from neopixel import NeoPixel
from micropython import const

# ── NeoPixel Setup ──────────────────────────────────────
dataPin = 18
pixels  = 10

np = NeoPixel(Pin(dataPin, Pin.OUT), pixels)
np.fill((0, 0, 0))
np.write()

# ── Servo Setup ─────────────────────────────────────────
servo = PWM(Pin(4), freq=50)

SERVO_OPEN_ANGLE  = 140
SERVO_CLOSE_ANGLE = 40

def angle_to_duty(angle):
    min_duty = 40
    max_duty = 115
    return int(min_duty + (angle / 180) * (max_duty - min_duty))

def openEyes():
    servo.duty(angle_to_duty(SERVO_OPEN_ANGLE))
    time.sleep(0.4)

def closeEyes():
    servo.duty(angle_to_duty(SERVO_CLOSE_ANGLE))
    time.sleep(0.4)

# ── BLE Setup ───────────────────────────────────────────
_IRQ_CENTRAL_CONNECT    = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE        = const(3)

_FLAG_READ    = const(0x0002)
_FLAG_WRITE   = const(0x0008)
_FLAG_NOTIFY  = const(0x0010)

SERVICE_UUID        = bluetooth.UUID("4fafc201-1fb5-459e-8fcc-c5c9c331914b")
CHARACTERISTIC_UUID = bluetooth.UUID("beb5483e-36e1-4688-b7f5-ea07361b26a8")

SERVICES = (
    (SERVICE_UUID, (
        (CHARACTERISTIC_UUID, _FLAG_READ | _FLAG_WRITE | _FLAG_NOTIFY),
    )),
)

class BLEESP32:
    def __init__(self):
        self._ble = bluetooth.BLE()
        self._ble.active(True)
        self._ble.irq(self._irq)
        ((self._handle,),) = self._ble.gatts_register_services(SERVICES)
        self._connected = False
        self._incoming  = None
        self._advertise()

    def is_connected(self):
        return self._connected

    def any(self):
        return self._incoming is not None

    def read(self):
        data = self._incoming
        self._incoming = None
        return data

    def send(self, msg):
        if self._connected:
            try:
                self._ble.gatts_notify(0, self._handle,
                                       msg.encode("utf-8"))
                print("Sent:", msg)
            except Exception as e:
                print("Send error:", e)

    def _irq(self, event, data):
        if event == _IRQ_CENTRAL_CONNECT:
            self._connected = True
            print("App connected!")
        elif event == _IRQ_CENTRAL_DISCONNECT:
            self._connected = False
            self._incoming  = None
            print("App disconnected! Restarting advertising...")
            self._advertise()
        elif event == _IRQ_GATTS_WRITE:
            value = self._ble.gatts_read(self._handle)
            self._incoming = value.decode("utf-8").strip()
            print(">>> Received from app:", self._incoming)

    def _advertise(self):
        name       = "EyeSpy"
        name_bytes = name.encode()
        payload    = bytearray()
        payload   += bytes([0x02, 0x01, 0x06])
        payload   += bytes([len(name_bytes) + 1, 0x09]) + name_bytes
        self._ble.gap_advertise(100, adv_data=payload)
        print("Advertising as:", name)

# ── Game Config ─────────────────────────────────────────
MAX_ROUNDS       = 5
THRESHOLD        = 80
FLASH_ON_MS      = 700
FLASH_OFF_MS     = 350
FLASH_COUNT      = 3
GUESS_TIME_LIMIT = 300000  # 5 minutes in ms

PALETTE = [
    "FF0000","00FF00","0000FF","FFFF00",
    "FF00FF","00FFFF","FF8000","8000FF",
    "FF0080","00FF80"
]

# ── Helper Functions ────────────────────────────────────
def hexToRgb(h):
    return (int(h[0:2],16), int(h[2:4],16), int(h[4:6],16))

def distance(c1, c2):
    return math.sqrt(
        (c1[0]-c2[0])**2 +
        (c1[1]-c2[1])**2 +
        (c1[2]-c2[2])**2
    )

def allOff():
    np.fill((0,0,0))
    np.write()

def flash(col, count):
    for _ in range(count):
        np.fill(col)
        np.write()
        time.sleep_ms(FLASH_ON_MS)
        allOff()
        time.sleep_ms(FLASH_OFF_MS)

# ── Startup ─────────────────────────────────────────────
print("Advertising as EyeSpy, waiting for connection...")
allOff()
closeEyes()

ble = BLEESP32()

while not ble.is_connected():
    time.sleep(0.2)

print("Connected! Starting game...")
ble.send("CONNECTED")
time.sleep(0.5)

openEyes()
ble.send("READY")

# ── Game Loop ───────────────────────────────────────────
round_num   = 1
gameRunning = True

while gameRunning:

    print("Round:", round_num)
    ble.send("ROUND:" + str(round_num))
    time.sleep(0.3)

    # Pick colour
    targetHex = random.choice(PALETTE)
    targetRgb = hexToRgb(targetHex)
    print("Target:", targetHex, "→ RGB:", targetRgb)

    # Show colour
    openEyes()
    flash(targetRgb, FLASH_COUNT)

    # Hide colour
    allOff()
    closeEyes()
    ble.send("WAIT")
    time.sleep(0.3)

    # ── Wait for guess (max 5 minutes) ──────────────────
    guess        = None
    startTime    = time.ticks_ms()
    lastTimeSent = -10000

    while guess is None:

        elapsed = time.ticks_diff(time.ticks_ms(), startTime)

        # Send countdown every 10 seconds
        if elapsed - lastTimeSent >= 10000:
            remaining    = (GUESS_TIME_LIMIT - elapsed) // 1000
            ble.send("TIME:" + str(remaining))
            lastTimeSent = elapsed
            print("Time remaining:", remaining, "s")

        # Time limit reached
        if elapsed > GUESS_TIME_LIMIT:
            print("Time up! Player loses.")
            ble.send("TIMEOUT")
            openEyes()
            flash((180, 0, 0), 5)
            closeEyes()
            gameRunning = False
            break

        # Check for incoming guess
        if ble.any():
            line = ble.read()
            print("Raw bytes:", [ord(c) for c in line])
            print("Processing line:", line)

            if line and "," in line:
                try:
                    # Strip all non-numeric and non-comma characters
                    cleaned = ""
                    for ch in line:
                        if ch.isdigit() or ch == ",":
                            cleaned += ch

                    print("Cleaned line:", cleaned)
                    parts = cleaned.split(",")

                    if len(parts) == 3 and all(len(p) > 0 for p in parts):
                        guess = (
                            int(parts[0]),
                            int(parts[1]),
                            int(parts[2])
                        )
                        print("Parsed guess:", guess)
                    else:
                        print("Bad parts:", parts)

                except Exception as e:
                    print("Parse error:", e)

        time.sleep_ms(50)

    if guess is None:
        continue

    # ── Compare ─────────────────────────────────────────
    openEyes()

    dist = distance(targetRgb, guess)
    print("Target RGB:", targetRgb)
    print("Guess RGB: ", guess)
    print("Distance:  ", dist)
    print("Threshold: ", THRESHOLD)

    if dist <= THRESHOLD:
        print("PASS!")
        ble.send("PASS")
        flash((0, 180, 0), 5)

        if round_num >= MAX_ROUNDS:
            ble.send("WINNER")
            print("YOU WIN!")
            closeEyes()
            gameRunning = False
        else:
            round_num += 1
            closeEyes()

    else:
        print("FAIL!")
        ble.send("FAIL")
        flash((180, 0, 0), 5)
        closeEyes()
        gameRunning = False

print("Game Ended")
ble.send("GAMEOVER")