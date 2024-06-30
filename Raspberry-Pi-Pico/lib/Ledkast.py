import neopixel
from lib.Effect import Effect

# Import all effects
from effects.chase_lights import ChaseLights
from effects.pulsate_leds import pulsateLEDs
from effects.start_up import startUpEffect

class Ledkast:
    def __init__(self, pin, ledCount):
        self.pin = pin
        self.ledCount = ledCount
        self.isActive = False
        self.isRunningEffect = False
        
        # We are misusing this to send the data using DMX cables to a seperate device
        # This is not the actual LED strip, but is used to generate a data signal that can
        # be distributed over to four ledstrips per ledkast.
        self.strips = neopixel.NeoPixel(pin, ledCount, auto_write=False)
        
    def startEffect(self, effect: Effect):
        self.isRunningEffect = False # Stop any running effects
        self.isActive = True

        if effect.name == "CHASE":
            ChaseLights(self.strips, self.isRunningEffect, self.ledCount, 50, effect.color)
        elif effect.name == "PULSATE":
            pulsateLEDs(self.strips, self.isRunningEffect, self.ledCount, effect.color)
        else:
            self.isActive = False
            print("⚠️ Invalid effect received. Skipping...")
            
    def clearLEDs(self):
        for i in range(self.ledCount):
            self.strips[i] = (0, 0, 0)
        self.strips.show()
        self.isActive = False
        
    def showStartupEffect(self):
        startUpEffect(self.strips)