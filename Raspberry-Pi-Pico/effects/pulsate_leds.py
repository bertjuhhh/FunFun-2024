import asyncio

async def pulsateLEDs(ledkast, color):
    brightness = 0
    direction = 1
    
    while ledkast.isRunningEffect:
        for i in range(ledkast.strips.n):
            ledkast.strips[i] = (color[0] * brightness // 255, color[1] * brightness // 255, color[2] * brightness // 255)
            
        ledkast.strips.write()
        
        brightness += direction
        
        if brightness <= 0 or brightness >= 255:
            direction *= -1
            
        await asyncio.sleep(0.01)