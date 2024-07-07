import asyncio
offset = 0
movingUp = True
brightness = 255

# Chase light config
LED_ON_OFF_COUNT = 1
SPACING = 1

async def ChaseLights(ledkast, color):
    global offset, movingUp, brightness
    speed = 200
    
    while ledkast.isRunningEffect:
        brightnessLevels = [20, 20, 75, 100, 150, 180, 255, 255, 255, 180, 150, 100, 75, 20, 20]

        for i in range(ledkast.strips.n):
            ledkast.strips[i] = (0, 0, 0)

        for i in range(ledkast.strips.n):
            for j in range(LED_ON_OFF_COUNT):
                brightness = brightnessLevels[j % len(brightnessLevels)]
                if (i + j + offset) < ledkast.strips.n:
                    ledkast.strips[i + j + offset] = color

        if movingUp:
            offset += 1
            if offset >= LED_ON_OFF_COUNT:
                movingUp = False
        else:
            offset -= 1
            if offset <= 0:
                movingUp = True

        ledkast.strips.write()
        await asyncio.sleep(speed / 100.0)