import neopixel
from lib.Effect import Effect
from machine import Pin 
import time

# Import all effects
from effects.chase_lights import ChaseLights
from effects.pulsate_leds import pulsateLEDs
from effects.start_up import startUpEffect
from effects.static import staticLEDs

class Ledkast:
    def __init__(self, pin, ledCount, name):
        self.pin = Pin(pin)
        self.name = name
        self.ledCount = ledCount
        self.isActive = False
        self.isRunningEffect = False
        
        # We are misusing this to send the data using DMX cables to a seperate device
        # This is not the actual LED strip, but is used to generate a data signal that can
        # be distributed over to four ledstrips per ledkast.
        self.strips = neopixel.NeoPixel(self.pin, ledCount)
        
    def startEffect(self, effect: Effect):
        # Clear the LEDs
        self.clearLEDs()
        
        time.sleep(1)
        
        self.isRunningEffect = True
        self.isActive = True
        
        if effect.name == "CHASE":
            ChaseLights(self.strips, self.isRunningEffect, self.ledCount, 50, effect.color)
        elif effect.name == "PULSATE":
            pulsateLEDs(self.strips, self.isRunningEffect, self.ledCount, effect.color)
        elif effect.name == "STATIC":
            print(f"Running static {effect.color}")
            staticLEDs(self.strips, effect.color)
        else:
            self.isActive = False
            print(f"⚠️ Invalid effect received. Skipping... {effect.name}")
            
    def clearLEDs(self):
        for i in range(self.strips.n):
            self.strips[i] = (0, 0, 0)
            
        self.strips.write()
        self.isActive = False
        
    def showStartupEffect(self):
        startUpEffect(self.strips)
