from lib.TimedEvent import TimedEvent
from lib.Effects import Effect
from lib.Groups import Groups
from lib.Colors import blue, gold, green, aquamarine

# typed array
eventLoop: list[TimedEvent] = []
pauzeLoop: list[TimedEvent] = []

def addEvent(start, end, effect: Effect, group, color = None):
    event = TimedEvent(start=start, end=end, effect=effect, group=group, color=color)
    eventLoop.append(event)
    
def addPauzeEvent(start, end, effect: Effect, group, color = None):
    event = TimedEvent(start=start, end=end, effect=effect, group=group, color=color)
    pauzeLoop.append(event)
    
# Times in milliseconds    
# 0 = infinite
addEvent(0, 0, Effect.PULSATE, Groups.LEDKAST_2, blue)

# PAUZE
addPauzeEvent(0, 4000, Effect.STATIC, Groups.LEDKAST_1, green)

addPauzeEvent(5000, 6000, Effect.STATIC, Groups.LEDKAST_3, gold)
addPauzeEvent(7000, 1000, Effect.STATIC, Groups.LEDKAST_3, aquamarine)

