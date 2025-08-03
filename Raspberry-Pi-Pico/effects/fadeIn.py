import asyncio


async def fadeInOut(ledkast, color, fade_speed=5):
    """
    Fade in effect followed by fade out.
    Gradually increases brightness from 0 to 255, then decreases back to 0.
    
    Args:
        ledkast: LED strip controller object
        color: RGB color tuple (r, g, b)
        fade_speed: Speed of fading (higher = faster)
    """
    brightness = 0
    
    # Fade in phase - gradually increase brightness
    while brightness < 255:
        # Apply current brightness to all LEDs
        for i in range(ledkast.strips.n):
            ledkast.strips[i] = (color[0] * brightness // 255, 
                                 color[1] * brightness // 255, 
                                 color[2] * brightness // 255)
            
        ledkast.strips.write()
        brightness += fade_speed
        
        # Ensure we don't exceed maximum brightness
        if brightness > 255:
            brightness = 255
            
        await asyncio.sleep(0.01)
    
    # Hold at full brightness briefly
    await asyncio.sleep(0.5)
    
    # Fade out phase - gradually decrease brightness
    while brightness > 0:
        # Apply current brightness to all LEDs
        for i in range(ledkast.strips.n):
            ledkast.strips[i] = (color[0] * brightness // 255, 
                                 color[1] * brightness // 255, 
                                 color[2] * brightness // 255)
            
        ledkast.strips.write()
        brightness -= fade_speed
        
        # Ensure we don't go below minimum brightness
        if brightness < 0:
            brightness = 0
            
        await asyncio.sleep(0.01)
    
    # Ensure all LEDs are completely off at the end
    for i in range(ledkast.strips.n):
        ledkast.strips[i] = (0, 0, 0)
        
    ledkast.strips.write()


async def fadeIn(ledkast, color, fade_speed=5):
    """
    Fade in effect only.
    Gradually increases brightness from 0 to 255.
    
    Args:
        ledkast: LED strip controller object
        color: RGB color tuple (r, g, b)
        fade_speed: Speed of fading (higher = faster)
    """
    brightness = 0
    
    # Fade in phase - gradually increase brightness
    while brightness < 255:
        # Apply current brightness to all LEDs
        for i in range(ledkast.strips.n):
            ledkast.strips[i] = (color[0] * brightness // 255, 
                                 color[1] * brightness // 255, 
                                 color[2] * brightness // 255)
            
        ledkast.strips.write()
        brightness += fade_speed
        
        # Ensure we don't exceed maximum brightness
        if brightness > 255:
            brightness = 255
            
        await asyncio.sleep(0.01)


async def fadeOut(ledkast, color, fade_speed=5):
    """
    Fade out effect only.
    Gradually decreases brightness from 255 to 0.
    
    Args:
        ledkast: LED strip controller object
        color: RGB color tuple (r, g, b)
        fade_speed: Speed of fading (higher = faster)
    """
    brightness = 255
    
    # Start with full brightness
    for i in range(ledkast.strips.n):
        ledkast.strips[i] = color
    ledkast.strips.write()
    
    # Fade out phase - gradually decrease brightness
    while brightness > 0:
        # Apply current brightness to all LEDs
        for i in range(ledkast.strips.n):
            ledkast.strips[i] = (color[0] * brightness // 255, 
                                 color[1] * brightness // 255, 
                                 color[2] * brightness // 255)
            
        ledkast.strips.write()
        brightness -= fade_speed
        
        # Ensure we don't go below minimum brightness
        if brightness < 0:
            brightness = 0
            
        await asyncio.sleep(0.01)
    
    # Ensure all LEDs are completely off at the end
    for i in range(ledkast.strips.n):
        ledkast.strips[i] = (0, 0, 0)
        
    ledkast.strips.write()