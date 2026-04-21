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
        data           = self._incoming
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
            value          = self._ble.gatts_read(self._handle)
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
FLASH_ON_MS      = 700
FLASH_OFF_MS     = 350
FLASH_COUNT      = 3
GUESS_TIME_LIMIT = 300000  # 5 minutes in ms

# Much more forgiving thresholds — especially round 1
# Distance is calculated across R, G, B so 255 = max possible per channel
THRESHOLDS = [180, 150, 120, 90, 60]

PALETTE = [
    "FF0000",  # red
    "00FF00",  # green
    "0000FF",  # blue
    "FFFF00",  # yellow
    "FF00FF",  # magenta
    "00FFFF",  # cyan
    "FF8000",  # orange
    "8000FF",  # purple
    "FF0080",  # pink
    "00FF80"   # mint
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

def waitForNext():
    print("Waiting for NEXT command from app...")
    ble.send("NEXT_PROMPT")
    while True:
        if ble.any():
            cmd = ble.read()
            print("Received:", cmd)
            if "NEXT" in cmd:
                break
        time.sleep_ms(100)

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
score       = 0
gameRunning = True

while gameRunning:

    print("─" * 30)
    print("Round:", round_num, "| Score:", score)
    print("Threshold:", THRESHOLDS[round_num - 1])
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
            print("Time up! Moving to next round anyway...")
            ble.send("TIMEOUT")
            openEyes()
            flash((180, 0, 0), 5)
            closeEyes()
            guess = (-1, -1, -1)  # dummy guess to exit loop
            break

        # Check for incoming guess
        if ble.any():
            line = ble.read()
            print("Raw bytes:", [ord(c) for c in line])
            print("Processing line:", line)

            if line and "," in line:
                try:
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

    # ── Compare ─────────────────────────────────────────
    openEyes()

    threshold = THRESHOLDS[round_num - 1]
    dist      = distance(targetRgb, guess)

    print("Target RGB:", targetRgb)
    print("Guess RGB: ", guess)
    print("Distance:  ", dist)
    print("Threshold: ", threshold)

    if dist <= threshold:
        score += 1
        print("PASS! Score:", score)
        ble.send("PASS:" + str(score))
        flash((0, 180, 0), 5)
        closeEyes()

        if round_num >= MAX_ROUNDS:
            # All rounds complete — winner!
            ble.send("WINNER:" + str(score))
            print("GAME COMPLETE! Final score:", score, "/", MAX_ROUNDS)
            gameRunning = False
        else:
            # Continue to next round
            waitForNext()
            round_num += 1

    else:
        print("FAIL! Score stays at:", score)
        ble.send("FAIL:" + str(score))
        flash((180, 0, 0), 5)
        closeEyes()

        if round_num >= MAX_ROUNDS:
            # Last round done even with fail
            ble.send("GAMEOVER:" + str(score))
            print("GAME COMPLETE! Final score:", score, "/", MAX_ROUNDS)
            gameRunning = False
        else:
            # Continue to next round despite fail
            waitForNext()
            round_num += 1

print("─" * 30)
print("Game Ended. Final Score:", score, "/", MAX_ROUNDS)
ble.send("GAMEOVER:" + str(score))