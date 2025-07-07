# You import all the IOs of your board
import board
import busio
# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306

print("ola")
# This is the main instance of your keyboard
keyboard = KMKKeyboard()
keyboard.debug_enabled = True
# Add the macro and oled extension
macros = Macros()
i2c_bus = busio.I2C(board.SCL, board.SDA)
driver = SSD1306(
    # Mandatory:
    i2c=i2c_bus,
    # Optional:
    device_address=0x3C,
)
display = Display(
    # Mandatory:
    display=driver,
    # Optional:
    width=128, # screen size
    height=32, # screen size
    flip = False, # flips your display content
    flip_left = False, # flips your display content on left side split
    flip_right = False, # flips your display content on right side split
    brightness=0.8, # initial screen brightness level
    brightness_step=0.1, # used for brightness increase/decrease keycodes
    dim_time=20, # time in seconds to reduce screen brightness
    dim_target=0.1, # set level for brightness decrease
    off_time=60, # time in seconds to turn off screen
    powersave_dim_time=10, # time in seconds to reduce screen brightness
    powersave_dim_target=0.1, # set level for brightness decrease
    powersave_off_time=30, # time in seconds to turn off screen
)
display.entries = [
    TextEntry(text="Hey there!", x=0, y=10),
]
keyboard.modules.append(macros)
keyboard.modules.append(display)
# Define your pins here!
PINS = [board.D7, board.D8, board.D9, board.D10, board.D2]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
    pull=True
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
        KC.E,
    ]
]
print("starting")
# Start kmk!
if __name__ == '__main__':
    print("it works!")
    keyboard.go()