import time

previousMillis = 0
brightness = 255
fadeAmount = -4
interval = 5
minBrightness = 20

def pulsateLEDs(strip, isRunning, ledCount, color):
    global previousMillis, brightness, fadeAmount, interval, minBrightness
    
    while isRunning:
        currentMillis = time.ticks_ms()
    
        if currentMillis - previousMillis >= interval:
            previousMillis = currentMillis
            brightness += fadeAmount

            if brightness <= minBrightness or brightness >= 255:
                fadeAmount = -fadeAmount

            for i in range(ledCount):
                strip[i] = color

            strip.brightness = brightness / 255.0

            strip.write()
