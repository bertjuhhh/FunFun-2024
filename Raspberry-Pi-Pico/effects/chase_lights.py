import asyncio

async def chase(ledkast, color, line_length=5, speed=0.05):
    position = 0
    direction = 1

    while True:
        # Clear the strip
        for i in range(ledkast.strips.n):
            ledkast.strips[i] = (0, 0, 0)

        # Draw the moving line
        for i in range(line_length):
            if 0 <= position + i < ledkast.strips.n:
                ledkast.strips[position + i] = color
        
        ledkast.strips.write()

        # Update position
        position += direction

        # Reverse direction at bounds
        if position <= 0:
            position = 0
            direction = 1
        elif position + line_length >= ledkast.strips.n:
            position = ledkast.strips.n - line_length
            direction = -1

        # Delay to control movement speed
        await asyncio.sleep(speed)
