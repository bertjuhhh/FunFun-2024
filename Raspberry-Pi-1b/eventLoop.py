from lib.TimedEvent import TimedEvent
from lib.Effects import Effect
from lib.Groups import Groups
from lib.Colors import blue, clear, lime, yellow, gold
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
    group1 = TimedEvent(start=0, effect=Effect.STATIC, group=Groups.ALL, color=clear)
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
addEvent(0, Effect.PULSATE, Groups.ALL, lime)
addEvent(46210, Effect.PULSATE, Groups.ALL, gold)
addEvent(111800, Effect.PULSATE, Groups.ALL, lime)

# PAUZE (Europapa)
clearAll(pauzeLoop)
addPauzeEvent(0, Effect.CHASE, Groups.ALL, orange)
addPauzeEvent(13200, Effect.FLASH, Groups.ALL, blue)
addPauzeEvent(14200, Effect.PULSATE, Groups.ALL, yellow)
addPauzeEvent(16800, Effect.FLASH, Groups.ALL, blue)
addPauzeEvent(17200, Effect.THEATER_CHASE_RAINBOW, Groups.ALL, blue)
addPauzeEvent(18200, Effect.FLASH, Groups.ALL, blue)
addPauzeEvent(18700, Effect.FLASH, Groups.ALL, blue)
addPauzeEvent(19500, Effect.FLASH, Groups.ALL, blue)
addPauzeEvent(25230, Effect.BPMFLASH, Groups.ALL, blue)
addPauzeEvent(43290, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(44750, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(46000, Effect.FLASH, Groups.ALL, yellow)

# verse marker
chorus1_start = 49140
addPauzeEvent(chorus1_start, Effect.BPMFLASH, Groups.ALL, blue)

addPauzeEvent(chorus1_start + 3560, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(chorus1_start + 3920, Effect.FLASH, Groups.ALL, yellow)

addPauzeEvent(chorus1_start + 5240, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(chorus1_start + 5680, Effect.FLASH, Groups.ALL, yellow)


addPauzeEvent(chorus1_start + 5900, Effect.BPMFLASH, Groups.ALL, blue)


addPauzeEvent(chorus1_start + 9640, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(chorus1_start + 10040, Effect.FLASH, Groups.ALL, yellow)

addPauzeEvent(chorus1_start + 11160, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(chorus1_start + 11510, Effect.FLASH, Groups.ALL, yellow)

addPauzeEvent(chorus1_start + 12500, Effect.BPMFLASH, Groups.ALL, blue)

addPauzeEvent(chorus1_start + 17380, Effect.FLASH, Groups.ALL, yellow)

addPauzeEvent(chorus1_start + 18200, Effect.BPMFLASH, Groups.ALL, blue)

# EU, RO, PA
addPauzeEvent(chorus1_start + 21130, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(chorus1_start + 21830, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(chorus1_start + 22590, Effect.FLASH, Groups.ALL, yellow)

addPauzeEvent(chorus1_start + 23600, Effect.FLASH, Groups.ALL, yellow)

addPauzeEvent(chorus1_start + 25000, Effect.BPMFLASH, Groups.ALL, blue)

verse2_marker = 73120

addPauzeEvent(verse2_marker + 0, Effect.BPMFLASH, Groups.ALL, blue)


chorus2_marker = 97190
addPauzeEvent(chorus2_marker, Effect.BPMFLASH, Groups.ALL, blue)

addPauzeEvent(chorus2_marker + 3560, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(chorus2_marker + 3920, Effect.FLASH, Groups.ALL, yellow)

addPauzeEvent(chorus2_marker + 5240, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(chorus2_marker + 5680, Effect.FLASH, Groups.ALL, yellow)


addPauzeEvent(chorus2_marker + 5900, Effect.BPMFLASH, Groups.ALL, blue)


addPauzeEvent(chorus2_marker + 9640, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(chorus2_marker + 10040, Effect.FLASH, Groups.ALL, yellow)

addPauzeEvent(chorus2_marker + 11160, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(chorus2_marker + 11510, Effect.FLASH, Groups.ALL, yellow)

addPauzeEvent(chorus2_marker + 12500, Effect.BPMFLASH, Groups.ALL, blue)

# EU, RO, PA
addPauzeEvent(chorus2_marker + 21130, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(chorus2_marker + 21830, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(chorus2_marker + 22590, Effect.FLASH, Groups.ALL, yellow)

addPauzeEvent(120000, Effect.PULSATE, Groups.ALL, yellow)
addPauzeEvent(133050, Effect.FLASH, Groups.ALL, yellow)

addPauzeEvent(135100, Effect.BPMFLASH, Groups.ALL, blue)
addPauzeEvent(146720, Effect.BPMFLASH, Groups.ALL, yellow)

addPauzeEvent(14967, Effect.BPMFLASH, Groups.ALL, blue)

addPauzeEvent(152010, Effect.FLASH, Groups.ALL, yellow)

addPauzeEvent(153070, Effect.BPMFLASH, Groups.ALL, blue)

ending_marker = 155720
addPauzeEvent(ending_marker + 0, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(ending_marker + 700, Effect.FLASH, Groups.ALL, yellow)
addPauzeEvent(ending_marker + 1400, Effect.FLASH, Groups.ALL, yellow)

# clear
addPauzeEvent(ending_marker + 1600, Effect.STATIC, Groups.ALL, clear)