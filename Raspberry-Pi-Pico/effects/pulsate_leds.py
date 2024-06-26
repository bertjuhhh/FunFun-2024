import time
from config import LED_COUNT, ledsBlue, ledsBlueTwo, interval, minBrightness

previousMillis = 0
brightness = 255
fadeAmount = -4

def pulsateLEDs(color):
    global previousMillis, brightness, fadeAmount
    currentMillis = time.monotonic() * 1000
    if currentMillis - previousMillis >= interval:
        previousMillis = currentMillis
        brightness += fadeAmount

        if brightness <= minBrightness or brightness >= 255:
            fadeAmount = -fadeAmount

        for i in range(LED_COUNT):
            ledsBlue[i] = color
            ledsBlueTwo[i] = color

        ledsBlue.brightness = brightness / 255.0
        ledsBlueTwo.brightness = brightness / 255.0

        ledsBlue.show()
        ledsBlueTwo.show()
