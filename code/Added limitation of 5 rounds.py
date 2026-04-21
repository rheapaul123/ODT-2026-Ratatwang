# ── Eye Spy — Full Game Code ────────────────────────────────────────────
# ESP32 + MicroPython
# Hardware:
#   GPIO 18  — NeoPixel ring (16 LEDs)
#   GPIO 4   — Servo 1 (upper eyelid)
#   GPIO 5   — Servo 2 (lower eyelid, mirrored)
#   GPIO 19  — Tactile button (active LOW, triggers game start)
#   BLE      — MIT App Inventor sends "R,G,B", receives PASS/FAIL/etc.

import bluetooth
import time
import math
import random
from machine import Pin, PWM
from neopixel import NeoPixel
from micropython import const

# ─────────────────────────────────────────────────────────────────────────
# NeoPixel
# ─────────────────────────────────────────────────────────────────────────
dataPin = 18
pixels  = 16

np = NeoPixel(Pin(dataPin, Pin.OUT), pixels)
np.fill((0, 0, 0))
np.write()

# ─────────────────────────────────────────────────────────────────────────
# Servo
# Reduced travel range to avoid overworking the motors:
#   CLOSED = 80°  (was 10°)
#   OPEN   = 50°  (was 120°)
# Servo 2 is mirrored: its angle = 180 - servo1 angle
#   CLOSED → 180 - 80 = 100°
#   OPEN   → 180 - 50 = 130°
# ─────────────────────────────────────────────────────────────────────────
SERVO1_OPEN_ANGLE  = 50
SERVO1_CLOSE_ANGLE = 80
SERVO2_OPEN_ANGLE  = 180 - SERVO1_OPEN_ANGLE    # 130
SERVO2_CLOSE_ANGLE = 180 - SERVO1_CLOSE_ANGLE   # 100

servo1 = PWM(Pin(4), freq=50)
servo2 = PWM(Pin(5), freq=50)

def angle_to_duty(angle):
    return int(40 + (angle / 180) * (115 - 40))

def openEyes():
    servo1.duty(angle_to_duty(SERVO1_OPEN_ANGLE))
    servo2.duty(angle_to_duty(SERVO2_OPEN_ANGLE))
    time.sleep_ms(400)

def closeEyes():
    servo1.duty(angle_to_duty(SERVO1_CLOSE_ANGLE))
    servo2.duty(angle_to_duty(SERVO2_CLOSE_ANGLE))
    time.sleep_ms(400)

def quickBlink():
    # a single natural-looking blink (close then reopen)
    servo1.duty(angle_to_duty(SERVO1_CLOSE_ANGLE))
    servo2.duty(angle_to_duty(SERVO2_CLOSE_ANGLE))
    time.sleep_ms(180)
    servo1.duty(angle_to_duty(SERVO1_OPEN_ANGLE))
    servo2.duty(angle_to_duty(SERVO2_OPEN_ANGLE))
    time.sleep_ms(120)

# ─────────────────────────────────────────────────────────────────────────
# Tactile Button  (GPIO 19, active LOW with internal pull-up)
# ─────────────────────────────────────────────────────────────────────────
button = Pin(19, Pin.IN, Pin.PULL_UP)

def buttonPressed():
    return button.value() == 0

# ─────────────────────────────────────────────────────────────────────────
# BLE
# ─────────────────────────────────────────────────────────────────────────
_IRQ_CENTRAL_CONNECT    = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE        = const(3)

_FLAG_READ   = const(0x0002)
_FLAG_WRITE  = const(0x0008)
_FLAG_NOTIFY = const(0x0010)

SERVICE_UUID        = bluetooth.UUID("4fafc201-1fb5-459e-8fcc-c5c9c331914b")
CHARACTERISTIC_UUID = bluetooth.UUID("beb5483e-36e1-4688-b7f5-ea07361b26a8")

SERVICES = (
    (SERVICE_UUID, (
        (CHARACTERISTIC_UUID, _FLAG_READ | _FLAG_WRITE | _FLAG_NOTIFY),
    )),
)

class BLEESP32:
    def __init__(self):
        self._ble       = bluetooth.BLE()
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
                self._ble.gatts_notify(0, self._handle, msg.encode("utf-8"))
                print("BLE sent:", msg)
            except Exception as e:
                print("BLE send error:", e)

    def _irq(self, event, data):
        if event == _IRQ_CENTRAL_CONNECT:
            self._connected = True
            print("App connected!")
        elif event == _IRQ_CENTRAL_DISCONNECT:
            self._connected = False
            self._incoming  = None
            print("App disconnected, re-advertising...")
            self._advertise()
        elif event == _IRQ_GATTS_WRITE:
            value          = self._ble.gatts_read(self._handle)
            self._incoming = value.decode("utf-8").strip()
            print("BLE received:", self._incoming)

    def _advertise(self):
        name       = "EyeSpy"
        name_bytes = name.encode()
        payload    = bytearray()
        payload   += bytes([0x02, 0x01, 0x06])
        payload   += bytes([len(name_bytes) + 1, 0x09]) + name_bytes
        self._ble.gap_advertise(100, adv_data=payload)
        print("Advertising as:", name)

# ─────────────────────────────────────────────────────────────────────────
# Colour Palette
# Vibrant hues at reduced brightness (~55-70%) so real-world photos
# at lower resolution still match accurately.
# ─────────────────────────────────────────────────────────────────────────
PALETTE = [
    (180,   0,   0),   # deep red
    (180,  60,   0),   # burnt orange
    (160, 120,   0),   # dark amber / gold
    (100, 160,   0),   # olive green
    (  0, 160,   0),   # forest green
    (  0, 160,  80),   # teal green
    (  0, 120, 160),   # ocean blue
    (  0,  60, 180),   # deep blue
    (100,   0, 160),   # deep purple
    (160,   0, 100),   # dark magenta
]

# ─────────────────────────────────────────────────────────────────────────
# Game Config
# ─────────────────────────────────────────────────────────────────────────
MAX_ROUNDS       = 5
FLASH_ON_MS      = 700
FLASH_OFF_MS     = 350
FLASH_COUNT      = 3
GUESS_TIME_LIMIT = 300000   # 5 minutes in ms

# Thresholds tighten each round
THRESHOLDS = [180, 150, 120, 90, 60]

# ─────────────────────────────────────────────────────────────────────────
# NeoPixel Helpers
# ─────────────────────────────────────────────────────────────────────────
def allOff():
    np.fill((0, 0, 0))
    np.write()

def flash(col, count, onMs=700, offMs=350):
    for _ in range(count):
        np.fill(col)
        np.write()
        time.sleep_ms(onMs)
        allOff()
        time.sleep_ms(offMs)

def hsv_to_rgb(h, s, v):
    # h: 0-360, s: 0-1, v: 0-1  →  (r, g, b) 0-255
    h = h % 360
    i = int(h / 60)
    f = (h / 60) - i
    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))
    if i == 0:   r, g, b = v, t, p
    elif i == 1: r, g, b = q, v, p
    elif i == 2: r, g, b = p, v, t
    elif i == 3: r, g, b = p, q, v
    elif i == 4: r, g, b = t, p, v
    else:        r, g, b = v, p, q
    return (int(r * 255), int(g * 255), int(b * 255))

# Rainbow snake state — global so idle loop resumes smoothly
_snake_offset = 0

def rainbowSnakeTick(speed=40):
    global _snake_offset
    snake_len = 6

    for i in range(pixels):
        pos = (i - _snake_offset) % pixels
        if pos < snake_len:
            hue        = (_snake_offset * 8 + i * (360 // pixels)) % 360
            brightness = 0.25 + 0.45 * ((snake_len - pos) / snake_len)
            r, g, b    = hsv_to_rgb(hue, 0.85, brightness)
            np[i]      = (r, g, b)
        else:
            np[i] = (0, 0, 0)

    np.write()
    _snake_offset = (_snake_offset + 1) % pixels
    time.sleep_ms(speed)

# ─────────────────────────────────────────────────────────────────────────
# Distance
# ─────────────────────────────────────────────────────────────────────────
def distance(c1, c2):
    return math.sqrt(
        (c1[0] - c2[0]) ** 2 +
        (c1[1] - c2[1]) ** 2 +
        (c1[2] - c2[2]) ** 2
    )

# ─────────────────────────────────────────────────────────────────────────
# Idle Mode — rainbow snake + occasional natural blink
# Runs until button is pressed, then returns.
# ─────────────────────────────────────────────────────────────────────────
def idleLoop():
    openEyes()
    print("Idle: rainbow snake + blinking. Press button to start.")
    ble.send("IDLE")

    nextBlink = time.ticks_ms() + random.randint(3000, 6000)

    while True:
        if buttonPressed():
            time.sleep_ms(50)       # debounce
            if buttonPressed():
                allOff()
                print("Button pressed — starting game!")
                return

        now = time.ticks_ms()
        if time.ticks_diff(now, nextBlink) >= 0:
            quickBlink()
            nextBlink = time.ticks_ms() + random.randint(3000, 7000)

        rainbowSnakeTick(speed=45)

# ─────────────────────────────────────────────────────────────────────────
# Boot
# ─────────────────────────────────────────────────────────────────────────
print("Booting Eye Spy...")
allOff()
closeEyes()

ble = BLEESP32()

print("Waiting for Bluetooth connection...")
while not ble.is_connected():
    rainbowSnakeTick(speed=80)

print("BLE connected!")
ble.send("CONNECTED")
time.sleep_ms(300)
ble.send("READY")

# ─────────────────────────────────────────────────────────────────────────
# Main outer loop — idle then game, repeat forever
# ─────────────────────────────────────────────────────────────────────────
while True:

    # ── Idle ─────────────────────────────────────────────────────────────
    idleLoop()

    # ── Game start ───────────────────────────────────────────────────────
    openEyes()
    ble.send("GAME_START")

    round_num   = 1
    score       = 0
    gameRunning = True

    while gameRunning:

        print("=" * 32)
        print("Round:", round_num, "of", MAX_ROUNDS,
              "| Score:", score,
              "| Threshold:", THRESHOLDS[round_num - 1])
        ble.send("ROUND:" + str(round_num))
        time.sleep_ms(300)

        # ── Pick colour ──────────────────────────────────────────────────
        targetRgb = random.choice(PALETTE)
        print("Target RGB:", targetRgb)

        # ── Anticipation pause ───────────────────────────────────────────
        closeEyes()
        time.sleep_ms(3000)

        # ── Reveal colour ────────────────────────────────────────────────
        openEyes()
        flash(targetRgb, FLASH_COUNT, FLASH_ON_MS, FLASH_OFF_MS)

        # ── Hide — player takes photo ────────────────────────────────────
        allOff()
        closeEyes()
        ble.send("WAIT")
        time.sleep_ms(300)

        # ── Wait for guess ───────────────────────────────────────────────
        guess        = None
        startTime    = time.ticks_ms()
        lastTimeSent = -10000

        while guess is None:
            elapsed = time.ticks_diff(time.ticks_ms(), startTime)

            # send countdown every 10 s
            if elapsed - lastTimeSent >= 10000:
                remaining    = (GUESS_TIME_LIMIT - elapsed) // 1000
                ble.send("TIME:" + str(remaining))
                lastTimeSent = elapsed
                print("Time remaining:", remaining, "s")

            # timeout after 5 minutes
            if elapsed > GUESS_TIME_LIMIT:
                print("Time up!")
                ble.send("TIMEOUT")
                openEyes()
                flash((160, 0, 0), 5, 200, 100)
                closeEyes()
                guess = (-1, -1, -1)
                break

            if ble.any():
                line = ble.read()
                print("Raw received:", line)
                if line and "," in line:
                    try:
                        cleaned = ""
                        for ch in line:
                            if ch.isdigit() or ch == ",":
                                cleaned += ch
                        parts = cleaned.split(",")
                        if len(parts) == 3 and all(len(p) > 0 for p in parts):
                            guess = (int(parts[0]), int(parts[1]), int(parts[2]))
                            print("Parsed guess:", guess)
                        else:
                            print("Bad parts:", parts)
                    except Exception as e:
                        print("Parse error:", e)

            time.sleep_ms(50)

        # ── Evaluate ─────────────────────────────────────────────────────
        openEyes()

        threshold = THRESHOLDS[round_num - 1]
        dist      = distance(targetRgb, guess)

        print("Target:", targetRgb, "| Guess:", guess,
              "| Distance:", round(dist, 1), "| Threshold:", threshold)

        if dist <= threshold:
            score += 1
            print("PASS! Score:", score)
            ble.send("PASS:" + str(score))
            flash((0, 160, 0), 5, 150, 80)      # fast green

            if round_num >= MAX_ROUNDS:
                ble.send("WINNER:" + str(score))
                print("GAME COMPLETE! Score:", score, "/", MAX_ROUNDS)
                gameRunning = False
            else:
                ble.send("NEXT_PROMPT")
                print("Waiting for NEXT from app...")
                while True:
                    if ble.any():
                        cmd = ble.read()
                        if cmd and "NEXT" in cmd:
                            break
                    time.sleep_ms(100)
                round_num += 1

        else:
            print("FAIL! Score stays:", score)
            ble.send("FAIL:" + str(score))
            flash((160, 0, 0), 5, 150, 80)      # fast red

            if round_num >= MAX_ROUNDS:
                ble.send("GAMEOVER:" + str(score))
                print("GAME COMPLETE! Score:", score, "/", MAX_ROUNDS)
                gameRunning = False
            else:
                ble.send("NEXT_PROMPT")
                print("Waiting for NEXT from app...")
                while True:
                    if ble.any():
                        cmd = ble.read()
                        if cmd and "NEXT" in cmd:
                            break
                    time.sleep_ms(100)
                round_num += 1

    # ── Game over — back to idle ──────────────────────────────────────────
    print("Back to idle...")
    ble.send("GAMEOVER:" + str(score))
    closeEyes()
    allOff()
    time.sleep_ms(1000)
    # outer while True loops back to idleLoop()