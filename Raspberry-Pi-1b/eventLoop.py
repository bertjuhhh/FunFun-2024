from lib.TimedEvent import TimedEvent
from lib.Effects import Effect
from lib.Groups import Groups
from lib.Colors import blue, gold, green, turquoise

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
addPauzeEvent(0, Effect.STATIC, Groups.LEDKAST_1, green)

addPauzeEvent(3900, Effect.STATIC, Groups.LEDKAST_1, gold)
addPauzeEvent(5900, Effect.STATIC, Groups.LEDKAST_1, turquoise)
addPauzeEvent(7900, Effect.CLEAR, Groups.LEDKAST_1)

