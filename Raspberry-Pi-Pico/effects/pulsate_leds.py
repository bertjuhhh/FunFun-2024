import asyncio

async def pulsateLEDs(ledkast, color):
    n = ledkast.strips.n
    current_led = 0
    
    while True:
        # Reset the entire strip to off
        for i in range(n):
            ledkast.strips[i] = (0, 0, 0)
        
        # Gradually light up the LEDs one by one
        for i in range(current_led):
            ledkast.strips[i] = color
        
        # Update the current LED position   
        current_led += 1
        
        # If we've reached the end of the strip, reset the position
        if current_led > n:
            current_led = 0
            
        ledkast.strips.write()
        await asyncio.sleep(0.05)