import time

from effects.pulsate_leds import pulsateLEDs

def startUpEffect(strip):
    for i in range(5):
        # Flash all LEDs red
        for i in range(strip.n):
            strip[i] = (255, 0, 0)
        strip.write()
        
        time.sleep(0.7)

        # Flash all LEDs green
        for i in range(strip.n):
            strip[i] = (0, 255, 0)
        strip.write()
            
        
        time.sleep(0.7)
         
        # Flash all LEDs blue
        for i in range(strip.n):
            strip[i] = (0, 0, 255)
        strip.write()
        
        time.sleep(0.7)
            