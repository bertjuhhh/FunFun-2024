import time
from config import LED_COUNT
offset = 0
movingUp = True
brightness = 255

# Chase light config
LED_ON_OFF_COUNT = 20
SPACING = 18

def ChaseLights(strip, isRunning, speed, color):
    global offset, movingUp, brightness
    while isRunning:
        brightnessLevels = [20, 20, 75, 100, 150, 180, 255, 255, 255, 180, 150, 100, 75, 20, 20]

        for i in range(LED_COUNT):
            strip[i] = (0, 0, 0)

        for i in range(LED_COUNT):
            for j in range(LED_ON_OFF_COUNT):
                brightness = brightnessLevels[j % len(brightnessLevels)]
                if (i + j + offset) < LED_COUNT:
                    strip[i + j + offset] = color

        if movingUp:
            offset += 1
            if offset >= LED_ON_OFF_COUNT:
                movingUp = False
        else:
            offset -= 1
            if offset <= 0:
                movingUp = True

        strip.show()
        time.sleep(speed / 100.0)
