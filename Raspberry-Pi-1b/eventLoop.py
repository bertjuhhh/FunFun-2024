from lib.TimedEvent import TimedEvent
from lib.Effects import Effect
from lib.Groups import zeelui, cartografen, windroos
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

#Main event loop
addToGroup(mainLoop, 0, Effect.PULSATE, windroos, blue)
addToGroup(mainLoop, 0, Effect.FADEIN, cartografen, gold)
addToGroup(mainLoop, 44000, Effect.FADEOUT, cartografen, gold)
addToGroup(mainLoop, 44000, Effect.FADEIN, zeelui, gold)
addToGroup(mainLoop, 83000, Effect.FADEIN, cartografen, gold)
addToGroup(mainLoop, 83000, Effect.FADEOUT, zeelui, gold)

# Example DIM effect usage:
# addToGroup(mainLoop, 90000, Effect.DIM, zeelui, blue)  # Dim to 25% brightness