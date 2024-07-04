from lib.TimedEvent import TimedEvent
from lib.Effects import Effect
from lib.Groups import Groups
from lib.Colors import blue, gold, green, turquoise, pink, red, clear, magenta
from lib.Groups import Groups

# typed array
eventLoop: list[TimedEvent] = []
pauzeLoop: list[TimedEvent] = []

def addEvent(start, effect: Effect, group, color = None):
    event = TimedEvent(start=start, effect=effect, group=group, color=color)
    eventLoop.append(event)
    
def addPauzeEvent(start, effect: Effect, group, color = None):
    event = TimedEvent(start=start, effect=effect, group=group, color=color)
    pauzeLoop.append(event)
    
def clearAll(loop):
    group1 = TimedEvent(start=0, effect=Effect.STATIC, group=Groups.LEDKAST_1, color=clear)
    group2 = TimedEvent(start=1000, effect=Effect.STATIC, group=Groups.LEDKAST_2, color=clear)
    group3 = TimedEvent(start=2000, effect=Effect.STATIC, group=Groups.LEDKAST_3, color=clear)
    group4 = TimedEvent(start=3000, effect=Effect.STATIC, group=Groups.LEDKAST_4, color=clear)
    
    loop.append(group1)
    loop.append(group2)
    loop.append(group3)
    loop.append(group4)
    
# Times in milliseconds    
# 0 = infinite
clearAll(eventLoop)
addEvent(6000, Effect.PULSATE, Groups.LEDKAST_2, blue)

# PAUZE
addPauzeEvent(5000, Effect.PULSATE, Groups.LEDKAST_1, red)
addPauzeEvent(5500, Effect.PULSATE, Groups.LEDKAST_2, green)
addPauzeEvent(6000, Effect.PULSATE, Groups.LEDKAST_3, turquoise)
addPauzeEvent(6500, Effect.PULSATE, Groups.LEDKAST_4, gold)

addPauzeEvent(13000, Effect.STATIC, Groups.LEDKAST_2, clear)
addPauzeEvent(18000, Effect.PULSATE, Groups.LEDKAST_2, magenta)

