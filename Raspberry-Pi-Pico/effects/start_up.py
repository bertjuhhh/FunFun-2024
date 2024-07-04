import asyncio

async def startUpEffect(strip):
    # Flash all LEDs red
    for i in range(strip.n):
        strip[i] = (255, 0, 0)
    strip.write()
    
    await asyncio.sleep(0.7)

    # Flash all LEDs green
    for i in range(strip.n):
        strip[i] = (0, 255, 0)
    strip.write()
    
    await asyncio.sleep(0.7)
        
    # Flash all LEDs blue
    for i in range(strip.n):
        strip[i] = (0, 0, 255)
    strip.write()
    
    await asyncio.sleep(0.7)
