import asyncio

async def chaseLEDs(ledkast, color, start_position, delay=0.05, fade_steps=10):
    n_leds = ledkast.strips.n
    position = start_position

    while True:
        for i in range(n_leds):
            ledkast.strips[i] = (0, 0, 0)  # Turn off all LEDs
            
        for j in range(n_leds):
            offset_position = (position + j) % n_leds
            fade_factor = max(0, (fade_steps - abs(j)) / fade_steps)
            ledkast.strips[offset_position] = (
                int(color[0] * fade_factor),
                int(color[1] * fade_factor),
                int(color[2] * fade_factor),
            )
        
        ledkast.strips.write()
        await asyncio.sleep(delay)
        
        # Move the chase position
        position = (position + 1) % n_leds

# Function to start multiple chases
async def chase(ledkast, color, num_chases=3, delay_between_chases=0.2):
    tasks = []
    for i in range(num_chases):
        start_position = (i * ledkast.strips.n // num_chases) % ledkast.strips.n
        tasks.append(asyncio.create_task(chaseLEDs(ledkast, color, start_position)))
        await asyncio.sleep(delay_between_chases)

    await asyncio.gather(*tasks)