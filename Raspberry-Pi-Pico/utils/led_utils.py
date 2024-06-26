from config import LED_COUNT, ledsBlue, ledsBlueTwo

def clearLEDs():
    for i in range(LED_COUNT):
        ledsBlue[i] = (0, 0, 0)
        ledsBlueTwo[i] = (0, 0, 0)
    ledsBlue.show()
    ledsBlueTwo.show()

def color_wheel(position):
    if position < 85:
        return (int(position * 3), int(255 - position * 3), 0)
    elif position < 170:
        position -= 85
        return (int(255 - position * 3), 0, int(position * 3))
    else:
        position -= 170
        return (0, int(position * 3), int(255 - position * 3))
