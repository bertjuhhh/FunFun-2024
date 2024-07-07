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

# verse marker
chorus1_start = 49140
addPauzeEvent(chorus1_start, Effect.BPMFLASH, Groups.LEDKAST_1, blue)

addPauzeEvent(chorus1_start + 3560, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(chorus1_start + 4000, Effect.FLASH, Groups.LEDKAST_1, yellow)

addPauzeEvent(chorus1_start + 5240, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(chorus1_start + 5680, Effect.FLASH, Groups.LEDKAST_1, yellow)


addPauzeEvent(chorus1_start + 5900, Effect.BPMFLASH, Groups.LEDKAST_1, blue)


addPauzeEvent(chorus1_start + 9640, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(chorus1_start + 10040, Effect.FLASH, Groups.LEDKAST_1, yellow)

addPauzeEvent(chorus1_start + 11160, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(chorus1_start + 11510, Effect.FLASH, Groups.LEDKAST_1, yellow)

addPauzeEvent(chorus1_start + 12500, Effect.BPMFLASH, Groups.LEDKAST_1, blue)

# EU, RO, PA
addPauzeEvent(chorus1_start + 21130, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(chorus1_start + 21830, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(chorus1_start + 22590, Effect.FLASH, Groups.LEDKAST_1, yellow)

verse2_marker = 73120

addPauzeEvent(verse2_marker + 0, Effect.BPMFLASH, Groups.LEDKAST_1, blue)


chorus2_marker = 97190
addPauzeEvent(chorus2_marker, Effect.BPMFLASH, Groups.LEDKAST_1, blue)

addPauzeEvent(chorus2_marker + 3560, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(chorus2_marker + 4000, Effect.FLASH, Groups.LEDKAST_1, yellow)

addPauzeEvent(chorus2_marker + 5240, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(chorus2_marker + 5680, Effect.FLASH, Groups.LEDKAST_1, yellow)


addPauzeEvent(chorus2_marker + 5900, Effect.BPMFLASH, Groups.LEDKAST_1, blue)


addPauzeEvent(chorus2_marker + 9640, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(chorus2_marker + 10040, Effect.FLASH, Groups.LEDKAST_1, yellow)

addPauzeEvent(chorus2_marker + 11160, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(chorus2_marker + 11510, Effect.FLASH, Groups.LEDKAST_1, yellow)

addPauzeEvent(chorus2_marker + 12500, Effect.BPMFLASH, Groups.LEDKAST_1, blue)

# EU, RO, PA
addPauzeEvent(chorus2_marker + 21130, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(chorus2_marker + 21830, Effect.FLASH, Groups.LEDKAST_1, yellow)
addPauzeEvent(chorus2_marker + 22590, Effect.FLASH, Groups.LEDKAST_1, yellow)
