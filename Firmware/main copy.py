import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


keyboard = Keyboard(usb_hid.devices)

switches = [
    (board.D10, Keycode.C, "Razor"),
    (board.D9, Keycode.V, "Selection"),
    (board.D8, Keycode.M, "Marker"),
]

buttons = []

for pin, key, name in switches:
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

buttons.append({
    "button": button,
    "key": key,
    "name": name,
    "last_state": True,
})

print ("Cut-Pad ready")

while True:
    or item in buttons:
    button = item ["button"]
    pressed = not button.value

    if pressed and item ["last_state"]:
        keyboard.send(item["key"])
        print(item["name"], "pressed")
        time.sleep(0.02)

    item["last_state"] = not pressed

time.sleep(0.005)
