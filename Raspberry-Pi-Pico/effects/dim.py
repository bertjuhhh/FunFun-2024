import asyncio


async def dim(ledkast, color, dim_level=64, fade_speed=3):
    """
    Dim effect - fades from full brightness down to a dimmed level.
    Does not turn LEDs completely off, just dims them.
    
    Args:
        ledkast: LED strip controller object
        color: RGB color tuple (r, g, b)
        dim_level: Final brightness level (0-255, default 64 = 25% brightness)
        fade_speed: Speed of dimming (higher = faster)
    """
    brightness = 255
    
    # Start with full brightness
    for i in range(ledkast.strips.n):
        ledkast.strips[i] = color
    ledkast.strips.write()
    
    # Brief pause at full brightness
    await asyncio.sleep(0.3)
    
    # Dim down to the specified level
    while brightness > dim_level:
        # Apply current brightness to all LEDs
        for i in range(ledkast.strips.n):
            ledkast.strips[i] = (color[0] * brightness // 255, 
                                 color[1] * brightness // 255, 
                                 color[2] * brightness // 255)
            
        ledkast.strips.write()
        brightness -= fade_speed
        
        # Ensure we don't go below the dim level
        if brightness < dim_level:
            brightness = dim_level
            
        await asyncio.sleep(0.02)
    
    # Set final dimmed state
    for i in range(ledkast.strips.n):
        ledkast.strips[i] = (color[0] * dim_level // 255, 
                             color[1] * dim_level // 255, 
                             color[2] * dim_level // 255)
        
    ledkast.strips.write()


async def dimToLevel(ledkast, color, start_level=255, end_level=64, fade_speed=3):
    """
    Dim effect with configurable start and end levels.
    Allows dimming from any brightness level to any other level.
    
    Args:
        ledkast: LED strip controller object
        color: RGB color tuple (r, g, b)
        start_level: Starting brightness level (0-255, default 255 = full)
        end_level: Ending brightness level (0-255, default 64 = 25% brightness)
        fade_speed: Speed of dimming (higher = faster)
    """
    brightness = start_level
    
    # Start with specified brightness
    for i in range(ledkast.strips.n):
        ledkast.strips[i] = (color[0] * brightness // 255, 
                             color[1] * brightness // 255, 
                             color[2] * brightness // 255)
    ledkast.strips.write()
    
    # Brief pause at start brightness
    await asyncio.sleep(0.2)
    
    # Determine direction (dimming down or brightening up)
    direction = -fade_speed if start_level > end_level else fade_speed
    
    # Fade to the target level
    while (direction < 0 and brightness > end_level) or (direction > 0 and brightness < end_level):
        # Apply current brightness to all LEDs
        for i in range(ledkast.strips.n):
            ledkast.strips[i] = (color[0] * brightness // 255, 
                                 color[1] * brightness // 255, 
                                 color[2] * brightness // 255)
            
        ledkast.strips.write()
        brightness += direction
        
        # Ensure we don't overshoot the target level
        if direction < 0 and brightness < end_level:
            brightness = end_level
        elif direction > 0 and brightness > end_level:
            brightness = end_level
            
        await asyncio.sleep(0.02)
    
    # Set final target state
    for i in range(ledkast.strips.n):
        ledkast.strips[i] = (color[0] * end_level // 255, 
                             color[1] * end_level // 255, 
                             color[2] * end_level // 255)
        
    ledkast.strips.write()