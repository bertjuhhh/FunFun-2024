from lib.TimedEvent import TimedEvent
from lib.DmxEvent import DmxEvent, addDmxToGroup, addDmxSingle
from lib.Effects import Effect
from lib.Groups import zeelui, cartografen, windroos, dmx_pars, dmx_wash, dmx_strobes, all_dmx_lights
from lib.Colors import blue, clear, lime, yellow, gold, dark_orange, red, green

# typed array
mainLoop: list[TimedEvent] = []
pauzeLoop: list[TimedEvent] = []
discoLoop: list[TimedEvent] = []

def addToGroup(loop, start, effect: Effect, group, color = None):
    for kast in group:
        loop.append(TimedEvent(start=start, effect=effect, group=kast, color=color))
    
def addSingle(loop, start, effect, kast, color):
    loop.append(TimedEvent(start=start, effect=effect, group=kast, color=color))
    
def addPauzeEvent(start, effect: Effect, group, color = None):
    addToGroup(pauzeLoop, start, effect, [group], color)

#Main event loop - LED effects
addToGroup(mainLoop, 0, Effect.PULSATE, windroos, blue)
addToGroup(mainLoop, 0, Effect.FADEIN, cartografen, gold)
addToGroup(mainLoop, 44000, Effect.FADEOUT, cartografen, gold)
addToGroup(mainLoop, 44000, Effect.FADEIN, zeelui, gold)
addToGroup(mainLoop, 83000, Effect.FADEIN, cartografen, gold)
addToGroup(mainLoop, 83000, Effect.FADEOUT, zeelui, gold)

# DMX effects in the main loop
addDmxToGroup(mainLoop, 0, Effect.DMX_FADE_UP, dmx_pars, red, intensity=255, duration=2000)
addDmxToGroup(mainLoop, 5000, Effect.DMX_COLOR, dmx_wash, blue, intensity=200)
addDmxToGroup(mainLoop, 10000, Effect.DMX_STROBE, dmx_strobes, color=None, strobe_speed=100, duration=3000)
addDmxToGroup(mainLoop, 20000, Effect.DMX_PULSE, dmx_pars, gold, intensity=255, duration=5000)
addDmxToGroup(mainLoop, 80000, Effect.DMX_BLACKOUT, all_dmx_lights)

# Example DIM effect usage:
# addToGroup(mainLoop, 90000, Effect.DIM, zeelui, blue)  # Dim to 25% brightness