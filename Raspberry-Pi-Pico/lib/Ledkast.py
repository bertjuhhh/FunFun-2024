import neopixel
from lib.Effect import Effect
from machine import Pin 
import asyncio
import time

# Import all effects
from effects.chase_lights import ChaseLights
from effects.start_up import startUpEffect
from effects.static import staticLEDs
from effects.pulsate_leds import pulsateLEDs
from effects.flash import flashLEDs
from effects.bpmflash import bpmflashLEDs

class Ledkast:
    def __init__(self, pin, ledCount, name):
        self.pin = Pin(pin)
        self.name = name
        self.ledCount = ledCount
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
                
        print(f"🚀 Starting effect {effect.name} on {self.name}")
        if effect.name == "CHASE":
            self.current_task = asyncio.create_task(ChaseLights(self, effect.color))
        elif effect.name == "PULSATE":
            self.current_task = asyncio.create_task(pulsateLEDs(self, effect.color))
        elif effect.name == "FLASH":
            self.current_task = asyncio.create_task(flashLEDs(self, effect.color))
        elif effect.name == "BPMFLASH":
            self.current_task = asyncio.create_task(bpmflashLEDs(self, effect.color, effect.bpm))
        elif effect.name == "STATIC":
            print(f"Running static {effect.color}")
            staticLEDs(self.strips, effect.color)
        elif effect.name == "CLEAR":
            self.clearLEDs()
        else:
            print(f"⚠️ Invalid effect received. Skipping... {effect.name}")
            
    def clearLEDs(self):
        for i in range(self.strips.n):
            self.strips[i] = (0, 0, 0)
            
        self.strips.write()
    
    async def showStartupEffect(self):
        print(f"🚀 Starting startup effect on {self.name}")
        startUpEffect(self.strips)