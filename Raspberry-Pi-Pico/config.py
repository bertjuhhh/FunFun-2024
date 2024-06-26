import board
import neopixel

# LED strip configuration:
LED_COUNT = 10
LED_PIN_BLUE = board.GP2
LED_PIN_BLUE_TWO = board.GP3
POTENTIOMETER_PIN = board.GP26
COLOR_POTENTIOMETER_PIN = board.GP27
INPUT_PIN = board.GP15
INPUT_PIN1 = board.GP14

# Create NeoPixel objects
ledsBlue = neopixel.NeoPixel(LED_PIN_BLUE, LED_COUNT, auto_write=False)
ledsBlueTwo = neopixel.NeoPixel(LED_PIN_BLUE_TWO, LED_COUNT, auto_write=False)

# Chase light config
LED_ON_OFF_COUNT = 20
SPACING = 18

# Pulsating config
interval = 5
minBrightness = 20
