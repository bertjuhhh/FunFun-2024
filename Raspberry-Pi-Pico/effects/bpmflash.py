import asyncio

# A effect that turns all leds on and off
async def bpmflashLEDs(ledkast, color, bpm):
    while True:
        for i in range(ledkast.strips.n):
            ledkast.strips[i] = color

        ledkast.strips.write()
        await asyncio.sleep(60 / bpm / 2)
        
        for i in range(ledkast.strips.n):
            ledkast.strips[i] = (0, 0, 0)

        ledkast.strips.write()
        await asyncio.sleep(60 / bpm / 2)