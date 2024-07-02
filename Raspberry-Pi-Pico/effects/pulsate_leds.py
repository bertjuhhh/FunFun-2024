import asyncio

async def pulsateLEDs(strips, isRunningEffect, color):
    brightness = 0
    direction = 1
    
    while isRunningEffect:
        for i in range(strips.n):
            strips[i] = (color[0] * brightness // 255, color[1] * brightness // 255, color[2] * brightness // 255)
            
        strips.write()
        
        brightness += direction
        
        if brightness <= 0 or brightness >= 255:
            direction *= -1
            
        await asyncio.sleep(0.01)