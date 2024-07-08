import asyncio


# TURN all ledson, then slowly turn them off
async def flashLEDs(ledkast, color):
    brightness = 255

    for i in range(ledkast.strips.n):
        ledkast.strips[i] = color
        
    ledkast.strips.write()
    
    # fade out
    while brightness >= 0:
        for i in range(ledkast.strips.n):
            ledkast.strips[i] = (color[0] * brightness // 255, color[1] * brightness // 255, color[2] * brightness // 255)
            
        ledkast.strips.write()
        
        brightness -= 10
        
        await asyncio.sleep(0.01)
        
    # clear
    
    for i in range(ledkast.strips.n):
        ledkast.strips[i] = (0, 0, 0)
        
    ledkast.strips.write()