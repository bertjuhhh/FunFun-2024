import random
import uasyncio as asyncio

def sample(population, k):
    """Return a k-length list of unique elements chosen from the population."""
    population = list(population)
    result = []
    for _ in range(k):
        idx = random.randint(0, len(population) - 1)
        result.append(population.pop(idx))
    return result

async def sparkle(ledkast, color, num_sparkles=10):
    while True:
        # Pick multiple random LEDs to sparkle
        sparkle_indices = sample(range(ledkast.strips.n), num_sparkles)
        
        tasks = []
        for index in sparkle_indices:
            # Create a task for each LED to sparkle independently
            task = asyncio.create_task(sparkle_led(ledkast, color, index))
            tasks.append(task)
        
        # Wait for all the sparkle tasks to complete
        await asyncio.gather(*tasks)

        # Pause before the next set of sparkles
        await asyncio.sleep(0.005)  # Reduced sleep duration for faster sparkles

async def sparkle_led(ledkast, color, index):
    # Faster fade in the LED
    for brightness in range(0, 256, 10):  # Increased step for faster brightness change
        ledkast.strips[index] = (brightness * color[0] // 255, 
                          brightness * color[1] // 255, 
                          brightness * color[2] // 255)
        ledkast.strips.write()
        await asyncio.sleep(0.005)  # Reduced sleep duration for faster transition

    # Faster fade out the LED
    for brightness in range(255, -1, -10):  # Increased step for faster brightness change
        ledkast.strips[index] = (brightness * color[0] // 255, 
                          brightness * color[1] // 255, 
                          brightness * color[2] // 255)
        ledkast.strips.write()
        await asyncio.sleep(0.005)  # Reduced sleep duration for faster transition
