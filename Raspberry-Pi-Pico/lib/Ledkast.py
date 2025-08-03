import neopixel
from lib.Effect import Effect
from machine import Pin
import asyncio
import time

# Import all effects
from effects.chase_lights import chase
from effects.start_up import startUpEffect
from effects.static import staticLEDs
from effects.pulsate_leds import pulsateLEDs
from effects.flash import flashLEDs
from effects.bpmflash import bpmflashLEDs
from effects.sparkle import sparkle
from effects.fadeIn import fadeInOut, fadeIn, fadeOut
from effects.dim import dim, dimToLevel

class Ledkast:
    def __init__(self, pin, ledCount, name):
        self.pin = Pin(pin)
        self.name = name
        self.ledCount = ledCount
        self.current_task = None
        
        # Initialize the LED strip (simulated as DMX signal generator)
        self.strips = neopixel.NeoPixel(self.pin, ledCount)
        
        # Effect mapping dictionary
        self.effect_map = {
            "CHASE": self._start_chase,
            "PULSATE": self._start_pulsate,
            "FLASH": self._start_flash,
            "BPMFLASH": self._start_bpmflash,
            "SPARKLE": self._start_sparkle,
            "STATIC": self._start_static,
            "CLEAR": self.clearLEDs,
            "FADE": self._start_fade,
            "FADEIN": self._start_fadein,
            "FADEOUT": self._start_fadeout,
            "DIM": self._start_dim,
        }
        
    async def startEffect(self, effect: Effect):
        if self.current_task:
            # Check if the current task is not done and needs to be canceled
            if not self.current_task.done():
                self.current_task.cancel()
                try:
                    await self.current_task
                except asyncio.CancelledError:
                    print("Previous effect cancelled")
                    
        self.clearLEDs()
        
        # Start the new effect if it exists in the map
        effect_func = self.effect_map.get(effect.name)
        if effect_func:
            print(f"🚀 Starting effect {effect.name} on {self.name}")
            if effect.name in ["STATIC", "CLEAR"]:
                # Direct call for non-coroutine functions
                effect_func(effect.color)
            else:
                # Schedule coroutine effect tasks
                self.current_task = asyncio.create_task(effect_func(effect))
        else:
            print(f"⚠️ Invalid effect received. Skipping... {effect.name}")

    def clearLEDs(self, color=(0, 0, 0)):
        self.strips.fill(color)
        self.strips.write()
    
    async def showStartupEffect(self):
        print(f"🚀 Starting startup effect on {self.name}")
        startUpEffect(self.strips)

    # Effect start methods
    async def _start_chase(self, effect: Effect):
        await chase(self, effect.color)

    async def _start_pulsate(self, effect: Effect):
        await pulsateLEDs(self, effect.color)

    async def _start_flash(self, effect: Effect):
        await flashLEDs(self, effect.color)

    async def _start_bpmflash(self, effect: Effect):
        await bpmflashLEDs(self, effect.color, effect.bpm)

    async def _start_sparkle(self, effect: Effect):
        await sparkle(self, effect.color)

    def _start_static(self, color):
        staticLEDs(self.strips, color)

    async def _start_fade(self, effect: Effect):
        await fadeInOut(self, effect.color)

    async def _start_fadein(self, effect: Effect):
        await fadeIn(self, effect.color)

    async def _start_fadeout(self, effect: Effect):
        await fadeOut(self, effect.color)

    async def _start_dim(self, effect: Effect):
        await dim(self, effect.color)

