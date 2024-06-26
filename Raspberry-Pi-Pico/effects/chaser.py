from lib.Effect import Effect
import time

# Chase light config
LED_ON_OFF_COUNT = 20
SPACING = 18
offset = 0
speed = 50
movingUp = True
LED_COUNT = 300

def callback(ledstrip, color):
    global offset, movingUp
    brightnessLevels = [20, 20, 75, 100, 150, 180, 255, 255, 255, 180, 150, 100, 75, 20, 20]

    # Turn off all LEDs
    for i in range(LED_COUNT):
        ledstrip[i] = (0, 0, 0)

    # Turn on the specified number of LEDs
    for i in range(LED_COUNT):
        for j in range(LED_ON_OFF_COUNT):
            brightness = brightnessLevels[j % len(brightnessLevels)]
            if (i + j + offset) < LED_COUNT:
                ledstrip[i + j + offset] = color

    if movingUp:
        offset += 1
        if offset >= LED_ON_OFF_COUNT:
            movingUp = False
    else:
        offset -= 1
        if offset <= 0:
            movingUp = True

    ledstrip.show()
    time.sleep(speed / 100.0)  # Adjust speed using the potentiometer
    
chaser = Effect("chaser", callback)