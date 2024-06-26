from lib.TimedEvent import TimedEvent
from lib.Effects import Effect
from lib.Groups import Groups
from lib.Colors import yellow

# typed array
eventLoop: list[TimedEvent] = []

def addEvent(start, end, effect: Effect, group, color = None):
    event = TimedEvent(start=start, end=end, effect=effect, group=group, color=color)
    eventLoop.append(event)
    
# Times in milliseconds    
# 0 = infinite
addEvent(0, 0, Effect.STATIC, Groups.LEDKAST_1, yellow)
addEvent(5000, 10000, Effect.RAINBOW, Groups.LEDKAST_1)
addEvent(10000, 15000, Effect.RAINBOW_CYCLE, Groups.LEDKAST_1)