import time
from config import LED_COUNT, LED_ON_OFF_COUNT, ledsBlue, ledsBlueTwo

offset = 0
movingUp = True

def ChaseLights(speed, color):
    global offset, movingUp
    brightnessLevels = [20, 20, 75, 100, 150, 180, 255, 255, 255, 180, 150, 100, 75, 20, 20]

    for i in range(LED_COUNT):
        ledsBlue[i] = (0, 0, 0)
        ledsBlueTwo[i] = (0, 0, 0)

    for i in range(LED_COUNT):
        for j in range(LED_ON_OFF_COUNT):
            brightness = brightnessLevels[j % len(brightnessLevels)]
            if (i + j + offset) < LED_COUNT:
                ledsBlue[i + j + offset] = color
                ledsBlueTwo[i + j + offset] = color

    if movingUp:
        offset += 1
        if offset >= LED_ON_OFF_COUNT:
            movingUp = False
    else:
        offset -= 1
        if offset <= 0:
            movingUp = True

    ledsBlue.show()
    ledsBlueTwo.show()
    time.sleep(speed / 100.0)
