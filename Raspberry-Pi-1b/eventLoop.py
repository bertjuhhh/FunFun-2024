from lib.TimedEvent import TimedEvent
from lib.Effects import Effect
from lib.Groups import Groups
from lib.Colors import blue, gold, green, turquoise, pink

# typed array
eventLoop: list[TimedEvent] = []
pauzeLoop: list[TimedEvent] = []

def addEvent(start, effect: Effect, group, color = None):
    event = TimedEvent(start=start, effect=effect, group=group, color=color)
    eventLoop.append(event)
    
def addPauzeEvent(start, effect: Effect, group, color = None):
    event = TimedEvent(start=start, effect=effect, group=group, color=color)
    pauzeLoop.append(event)
    
# Times in milliseconds    
# 0 = infinite
addEvent(0, Effect.PULSATE, Groups.LEDKAST_2, blue)

# PAUZE
addPauzeEvent(0, Effect.PULSATE, Groups.LEDKAST_2, green)
addPauzeEvent(8000, Effect.CLEAR, Groups.LEDKAST_1)
addPauzeEvent(10000, Effect.PULSATE, Groups.LEDKAST_2, pink)

