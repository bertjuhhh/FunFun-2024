import asyncio
import random

# Custom shuffle function
def custom_shuffle(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]

async def sparkle(ledbox, sparkle_color, fade_steps=15, delay=0.01):
    while True:
        # Create a list of all LED indices
        indices = list(range(ledbox.strips.n))
        
        # Custom shuffle to randomize the order
        custom_shuffle(indices)
        
        # Turn on LEDs one by one quickly
        for led_index in indices:
            # Gradually increase the brightness for the current LED
            for brightness in range(0, 256, fade_steps):
                ledbox.strips[led_index] = (
                    sparkle_color[0] * brightness // 255,
                    sparkle_color[1] * brightness // 255,
                    sparkle_color[2] * brightness // 255
                )
            ledbox.strips.write()
            await asyncio.sleep(delay)
        
        # Small pause when all LEDs are fully lit
        await asyncio.sleep(0.2)
        
        # Custom shuffle to randomize the order for fading out
        custom_shuffle(indices)
        
        # Turn off LEDs one by one quickly
        for led_index in indices:
            # Gradually decrease the brightness for the current LED
            for brightness in range(255, -1, -fade_steps):
                ledbox.strips[led_index] = (
                    sparkle_color[0] * brightness // 255,
                    sparkle_color[1] * brightness // 255,
                    sparkle_color[2] * brightness // 255
                )
            ledbox.strips.write()
            await asyncio.sleep(delay)
        
        # Small pause when all LEDs are off
        await asyncio.sleep(0.2)

# Example usage
# Assuming you have initialized `ledbox` and it supports n LEDs:
# sparkle_color = (255, 255, 255)  # White sparkle
# asyncio.run(sparkle_loop(ledbox, sparkle_color))

