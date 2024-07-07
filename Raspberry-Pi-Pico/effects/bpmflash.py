import asyncio

async def bpmflashLEDs(ledkast, color, bpm):
    brightness = 0
    direction = 1
    speed = 60 / bpm
    
    while ledkast.isRunningEffect:
        for i in range(ledkast.strips.n):
            ledkast.strips[i] = (color[0] * brightness // 255, color[1] * brightness // 255, color[2] * brightness // 255)
            
        ledkast.strips.write()
        
        brightness += direction
        
        if brightness <= 0 or brightness >= 255:
            direction *= -1
            
        await asyncio.sleep(speed / 100.0)