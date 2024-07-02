import neopixel
from lib.Effect import Effect
from machine import Pin 
import uasyncio as asyncio

# Import all effects
from effects.chase_lights import ChaseLights
from effects.start_up import startUpEffect
from effects.static import staticLEDs
from effects.pulsate_leds import pulsateLEDs

class Ledkast:
    def __init__(self, pin, ledCount, name):
        self.pin = Pin(pin)
        self.name = name
        self.ledCount = ledCount
        self.isActive = False
        self.isRunningEffect = False
        self.current_task = None
        
        # We are misusing this to send the data using DMX cables to a separate device
        # This is not the actual LED strip, but is used to generate a data signal that can
        # be distributed over to four ledstrips per ledkast.
        self.strips = neopixel.NeoPixel(self.pin, ledCount)
        
    async def startEffect(self, effect: Effect):
        # Cancel any existing effect task
        if self.current_task is not None:
            self.current_task.cancel()
            try:
                await self.current_task
            except asyncio.CancelledError:
                print("Previous effect cancelled")
        
        self.clearLEDs()
        self.isRunningEffect = False
        
        self.isRunningEffect = True
        self.isActive = True
        
        if effect.name == "CHASE":
            self.current_task = asyncio.create_task(ChaseLights(self.strips, self.isRunningEffect, self.ledCount, 50, effect.color))
        elif effect.name == "PULSATE":
            self.current_task = asyncio.create_task(pulsateLEDs(self.strips, self.isRunningEffect, effect.color))
        elif effect.name == "STATIC":
            print(f"Running static {effect.color}")
            staticLEDs(self.strips, effect.color)
            self.isRunningEffect = False
        elif effect.name == "CLEAR":
            self.clearLEDs()
            self.isRunningEffect = False
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