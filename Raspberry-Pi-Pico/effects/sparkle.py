import asyncio
import random

async def sparkle(ledkast, color, num_sparkles=10):
    while True:
        # Pick multiple random LEDs to sparkle
        sparkle_indices = random.sample(range(len(ledkast)), num_sparkles)
        
        tasks = []
        for index in sparkle_indices:
            # Create a task for each LED to sparkle independently
            task = asyncio.create_task(sparkle_led(ledkast, color, index))
            tasks.append(task)
        
        # Wait for all the sparkle tasks to complete
        await asyncio.gather(*tasks)

        # Pause before the next set of sparkles
        await asyncio.sleep(random.uniform(0.1, 0.5))

async def sparkle_led(ledkast, color, index):
    # Fade in the LED
    for brightness in range(0, 256, 5):
        ledkast[index] = (brightness * color[0] // 255, 
                          brightness * color[1] // 255, 
                          brightness * color[2] // 255)
        ledkast.strips.write()
        await asyncio.sleep(0.01)

    # Fade out the LED
    for brightness in range(255, -1, -5):
        ledkast.strips[index] = (brightness * color[0] // 255, 
                          brightness * color[1] // 255, 
                          brightness * color[2] // 255)
        ledkast.strips.write()
        await asyncio.sleep(0.01)

# Example usage:
# asyncio.run(sparkle(ledstrip, (255, 255, 255), num_sparkles=20))  # Sparkle 20 LEDs with white color
