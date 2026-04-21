# ── Imports ─────────────────────────────────────────────
from machine import Pin
from neopixel import NeoPixel
from servo import Servo
import time
import math
import random
from simple_ble import BLEConnection   # rename your BLE class file to this

# ── NeoPixel Setup ──────────────────────────────────────
dataPin = 18
pixels  = 10

np = NeoPixel(Pin(dataPin, Pin.OUT), pixels)
np.fill((0, 0, 0))
np.write()

# ── Servo Setup ─────────────────────────────────────────
servoPin = Pin(4, Pin.OUT)
pupilservo = Servo(servoPin)

SERVO_OPEN_ANGLE  = 140
SERVO_CLOSE_ANGLE = 40

def openEyes():
    pupilservo.write_angle(SERVO_OPEN_ANGLE)
    time.sleep(0.4)

def closeEyes():
    pupilservo.write_angle(SERVO_CLOSE_ANGLE)
    time.sleep(0.4)

# ── BLE Setup ───────────────────────────────────────────
ble = BLEConnection("EyeSpy_")

btBuffer = ""

def btReadline():
    global btBuffer
    if ble.any():
        data = ble.read()
        btBuffer += data
        
        if "\n" in btBuffer:
            line, btBuffer = btBuffer.split("\n", 1)
            return line.strip()
    return None

def btWrite(msg):
    ble.send_array([msg])   # sends as string

# ── Game Config ─────────────────────────────────────────
MAX_ROUNDS   = 5
THRESHOLD    = 80

FLASH_ON_MS  = 700
FLASH_OFF_MS = 350
FLASH_COUNT  = 3

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
print("Eye Spy Starting...")
allOff()
openEyes()

btWrite("READY")

# ── Game Loop ───────────────────────────────────────────
round_num = 1
gameRunning = True

while gameRunning:

    print("Round:", round_num)
    btWrite("ROUND:" + str(round_num))

    # Pick colour
    targetHex = random.choice(PALETTE)
    targetRgb = hexToRgb(targetHex)

    print("Target:", targetHex)
    btWrite("TARGET:" + targetHex)

    # Show colour
    openEyes()
    flash(targetRgb, FLASH_COUNT)

    # Hide colour
    allOff()
    closeEyes()
    btWrite("WAIT")

    # Wait for guess
    guess = None

    while guess is None:
        ble.check_timeout()

        line = btReadline()
        if line:
            try:
                parts = line.split(",")
                if len(parts) == 3:
                    guess = (int(parts[0]), int(parts[1]), int(parts[2]))
                    print("Guess:", guess)
            except:
                print("Bad input")

        time.sleep_ms(50)

    # Reveal
    openEyes()

    # Check answer
    dist = distance(targetRgb, guess)
    print("Distance:", dist)

    if dist <= THRESHOLD:
        print("PASS")
        btWrite("PASS")
        flash((0,180,0), 5)

        if round_num >= MAX_ROUNDS:
            btWrite("WINNER")
            print("YOU WIN")
            closeEyes()
            gameRunning = False
        else:
            round_num += 1

    else:
        print("FAIL")
        btWrite("FAIL")
        flash((180,0,0), 5)
        closeEyes()
        gameRunning = False

print("Game Ended")