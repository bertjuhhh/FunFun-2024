from lib.TimedEvent import TimedEvent
from lib.Effects import Effect
from lib.Groups import Groups
from lib.Colors import blue, gold, green, turquoise, pink, red, clear, magenta, orange, yellow
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
    group2 = TimedEvent(start=0, effect=Effect.STATIC, group=Groups.LEDKAST_2, color=clear)
    group3 = TimedEvent(start=0, effect=Effect.STATIC, group=Groups.LEDKAST_3, color=clear)
    group4 = TimedEvent(start=0, effect=Effect.STATIC, group=Groups.LEDKAST_4, color=clear)
    
    loop.append(group1)
    loop.append(group2)
    loop.append(group3)
    loop.append(group4)
    
# Currently, only STATIC and PULSATE are supported
# Times in milliseconds    
# 0 = infinite
clearAll(eventLoop)
addEvent(1000, Effect.STATIC, Groups.LEDKAST_2, red)
addEvent(2000, Effect.STATIC, Groups.LEDKAST_2, orange)
addEvent(3000, Effect.PULSATE, Groups.LEDKAST_2, blue)

# PAUZE (Europapa)
clearAll(pauzeLoop)
addPauzeEvent(0, Effect.PULSATE, Groups.LEDKAST_1, blue)
addPauzeEvent(13200, Effect.FLASH, Groups.LEDKAST_1, blue)
addPauzeEvent(14200, Effect.PULSATE, Groups.LEDKAST_1, yellow)
addPauzeEvent(16800, Effect.FLASH, Groups.LEDKAST_1, blue)
addPauzeEvent(17200, Effect.FLASH, Groups.LEDKAST_1, blue)
addPauzeEvent(18200, Effect.FLASH, Groups.LEDKAST_1, blue)
addPauzeEvent(18700, Effect.FLASH, Groups.LEDKAST_1, blue)
addPauzeEvent(19500, Effect.FLASH, Groups.LEDKAST_1, blue)
addPauzeEvent(25230, Effect.BPMFLASH, Groups.LEDKAST_1, blue)
addPauzeEvent(43290, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(44750, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(46000, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(49140, Effect.BPMFLASH, Groups.LEDKAST_1, blue)

addPauzeEvent(52800, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(53180, Effect.FLASH, Groups.LEDKAST_1, yellow)

addPauzeEvent(54380, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(54680, Effect.FLASH, Groups.LEDKAST_1, yellow)

addPauzeEvent(55040, Effect.BPMFLASH, Groups.LEDKAST_1, blue)


