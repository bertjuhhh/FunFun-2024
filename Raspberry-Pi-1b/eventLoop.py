from lib.TimedEvent import TimedEvent
from lib.Effects import Effect
from lib.Groups import Groups
from lib.Colors import blue, gold

# typed array
eventLoop: list[TimedEvent] = []

def addEvent(start, end, effect: Effect, group, color = None):
    event = TimedEvent(start=start, end=end, effect=effect, group=group, color=color)
    eventLoop.append(event)
    
# Times in milliseconds    
# 0 = infinite
addEvent(0, 0, Effect.PULSATE, Groups.LEDKAST_2, blue)
addEvent(0, 0, Effect.PULSATE, Groups.LEDKAST_3, blue)

addEvent(5000, 10000, Effect.CHASE, Groups.LEDKAST_2, gold)
addEvent(5000, 10000, Effect.CHASE, Groups.LEDKAST_3, gold)

addEvent(12000, 20000, Effect.PULSATE, Groups.LEDKAST_2, blue)
addEvent(12000, 20000, Effect.PULSATE, Groups.LEDKAST_3, blue)