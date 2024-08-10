import asyncio

async def pulsateLEDs(ledkast, color):
    brightness = 0
    direction = 8
        
    while True:
        # Update the color of each LED with the current brightness
        for i in range(ledkast.strips.n):
            ledkast.strips[i] = (color[0] * brightness // 255, 
                                 color[1] * brightness // 255, 
                                 color[2] * brightness // 255)
            
        ledkast.strips.write()
        
        # Update brightness
        brightness += direction
        
        # Reverse direction at bounds
        if brightness <= 0:
            brightness = 0
            direction = 8
        elif brightness >= 255:
            brightness = 255
            direction = -8
            
        # Delay to control pulsation speed
        await asyncio.sleep(0.001)

