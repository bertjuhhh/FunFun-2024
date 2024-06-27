import time
from config import LED_COUNT

previousMillis = 0
brightness = 255
fadeAmount = -4
interval = 5
minBrightness = 20

def pulsateLEDs(strip, isRunning, color):
    while isRunning:
        currentMillis = time.monotonic() * 1000
    
        if currentMillis - previousMillis >= interval:
            previousMillis = currentMillis
            brightness += fadeAmount

            if brightness <= minBrightness or brightness >= 255:
                fadeAmount = -fadeAmount

            for i in range(LED_COUNT):
                strip[i] = color

            strip.brightness = brightness / 255.0

            strip.show()
