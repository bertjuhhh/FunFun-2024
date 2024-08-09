from lib.TimedEvent import TimedEvent
from lib.Effects import Effect
from lib.Kasten import KASTEN
from lib.Groups import outside_group, internal_indicators
from lib.Colors import blue, clear, lime, yellow, gold, orange, red

# typed array
eventLoop: list[TimedEvent] = []
pauzeLoop: list[TimedEvent] = []
discoLoop: list[TimedEvent] = []

def addEventToLoop(loop, start, effect: Effect, group, color = None):
    for kast in group:
        loop.append(TimedEvent(start=start, effect=effect, group=kast, color=color))
    
def addPauzeEvent(start, effect: Effect, group, color = None):
    addEventToLoop(pauzeLoop, start, effect, [group], color)
    
def clearAll(loop):
    group1 = TimedEvent(start=0, effect=Effect.STATIC, group=KASTEN.ALL, color=clear)
    group2 = TimedEvent(start=0, effect=Effect.STATIC, group=KASTEN.LEDKAST_2, color=clear)
    group3 = TimedEvent(start=0, effect=Effect.STATIC, group=KASTEN.LEDKAST_3, color=clear)
    group4 = TimedEvent(start=0, effect=Effect.STATIC, group=KASTEN.LEDKAST_4, color=clear)
    group1b = TimedEvent(start=0, effect=Effect.STATIC, group=KASTEN.LEDKAST_1b, color=clear)
    group2b = TimedEvent(start=0, effect=Effect.STATIC, group=KASTEN.LEDKAST_2b, color=clear)
    group3b = TimedEvent(start=0, effect=Effect.STATIC, group=KASTEN.LEDKAST_3b, color=clear)
    group4b = TimedEvent(start=0, effect=Effect.STATIC, group=KASTEN.LEDKAST_4b, color=clear)
    
    loop.append(group1)
    loop.append(group2)
    loop.append(group3)
    loop.append(group4)
    loop.append(group1b)
    loop.append(group2b)
    loop.append(group3b)
    loop.append(group4b)
    
# Currently, only STATIC, FLASH and PULSATE are supported
# Times in milliseconds    
# 0 = infinite

clearAll(eventLoop)
addEventToLoop(eventLoop, 0, Effect.PULSATE, outside_group, lime)
addEventToLoop(eventLoop, 46210, Effect.PULSATE, outside_group, gold)
addEventToLoop(eventLoop, 111800, Effect.PULSATE, outside_group, lime)

# BEWEGERS INDICATOREN
addEventToLoop(eventLoop, 0, Effect.STATIC, internal_indicators, red)
addEventToLoop(eventLoop, 22000, Effect.STATIC, internal_indicators, orange)
addEventToLoop(eventLoop, 27000, Effect.PULSATE, internal_indicators, gold)

addEventToLoop(eventLoop, 40000, Effect.STATIC, internal_indicators, orange)
addEventToLoop(eventLoop, 45000, Effect.PULSATE, internal_indicators, yellow)

addEventToLoop(eventLoop, 65000, Effect.STATIC, internal_indicators, orange)
addEventToLoop(eventLoop, 70000, Effect.PULSATE, internal_indicators, lime)

addEventToLoop(eventLoop, 85000, Effect.STATIC, internal_indicators, orange)
addEventToLoop(eventLoop, 90000, Effect.STATIC, internal_indicators, red)

# PAUZE (Europapa)
clearAll(pauzeLoop)
addPauzeEvent(0, Effect.CHASE, KASTEN.ALL, orange)
addPauzeEvent(13200, Effect.FLASH, KASTEN.ALL, blue)
addPauzeEvent(14200, Effect.PULSATE, KASTEN.ALL, yellow)
addPauzeEvent(16800, Effect.FLASH, KASTEN.ALL, blue)
addPauzeEvent(17200, Effect.THEATER_CHASE_RAINBOW, KASTEN.ALL, blue)
addPauzeEvent(18200, Effect.FLASH, KASTEN.ALL, blue)
addPauzeEvent(18700, Effect.FLASH, KASTEN.ALL, blue)
addPauzeEvent(19500, Effect.FLASH, KASTEN.ALL, blue)
addPauzeEvent(25230, Effect.BPMFLASH, KASTEN.ALL, blue)
addPauzeEvent(43290, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(44750, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(46000, Effect.FLASH, KASTEN.ALL, yellow)

# verse marker
chorus1_start = 49140
addPauzeEvent(chorus1_start, Effect.BPMFLASH, KASTEN.ALL, blue)

addPauzeEvent(chorus1_start + 3560, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(chorus1_start + 3920, Effect.FLASH, KASTEN.ALL, yellow)

addPauzeEvent(chorus1_start + 5240, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(chorus1_start + 5680, Effect.FLASH, KASTEN.ALL, yellow)


addPauzeEvent(chorus1_start + 5900, Effect.BPMFLASH, KASTEN.ALL, blue)


addPauzeEvent(chorus1_start + 9640, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(chorus1_start + 10040, Effect.FLASH, KASTEN.ALL, yellow)

addPauzeEvent(chorus1_start + 11160, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(chorus1_start + 11510, Effect.FLASH, KASTEN.ALL, yellow)

addPauzeEvent(chorus1_start + 12500, Effect.BPMFLASH, KASTEN.ALL, blue)

addPauzeEvent(chorus1_start + 17380, Effect.FLASH, KASTEN.ALL, yellow)

addPauzeEvent(chorus1_start + 18200, Effect.BPMFLASH, KASTEN.ALL, blue)

# EU, RO, PA
addPauzeEvent(chorus1_start + 21130, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(chorus1_start + 21830, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(chorus1_start + 22590, Effect.FLASH, KASTEN.ALL, yellow)

addPauzeEvent(chorus1_start + 23600, Effect.FLASH, KASTEN.ALL, yellow)

addPauzeEvent(chorus1_start + 25000, Effect.BPMFLASH, KASTEN.ALL, blue)

verse2_marker = 73120

addPauzeEvent(verse2_marker + 0, Effect.BPMFLASH, KASTEN.ALL, blue)


chorus2_marker = 97190
addPauzeEvent(chorus2_marker, Effect.BPMFLASH, KASTEN.ALL, blue)

addPauzeEvent(chorus2_marker + 3560, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(chorus2_marker + 3920, Effect.FLASH, KASTEN.ALL, yellow)

addPauzeEvent(chorus2_marker + 5240, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(chorus2_marker + 5680, Effect.FLASH, KASTEN.ALL, yellow)


addPauzeEvent(chorus2_marker + 5900, Effect.BPMFLASH, KASTEN.ALL, blue)


addPauzeEvent(chorus2_marker + 9640, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(chorus2_marker + 10040, Effect.FLASH, KASTEN.ALL, yellow)

addPauzeEvent(chorus2_marker + 11160, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(chorus2_marker + 11510, Effect.FLASH, KASTEN.ALL, yellow)

addPauzeEvent(chorus2_marker + 12500, Effect.BPMFLASH, KASTEN.ALL, blue)

# EU, RO, PA
addPauzeEvent(chorus2_marker + 21130, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(chorus2_marker + 21830, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(chorus2_marker + 22590, Effect.FLASH, KASTEN.ALL, yellow)

addPauzeEvent(120000, Effect.PULSATE, KASTEN.ALL, yellow)
addPauzeEvent(133050, Effect.FLASH, KASTEN.ALL, yellow)

addPauzeEvent(135100, Effect.BPMFLASH, KASTEN.ALL, blue)
addPauzeEvent(146720, Effect.BPMFLASH, KASTEN.ALL, yellow)

addPauzeEvent(14967, Effect.BPMFLASH, KASTEN.ALL, blue)

addPauzeEvent(152010, Effect.FLASH, KASTEN.ALL, yellow)

addPauzeEvent(153070, Effect.BPMFLASH, KASTEN.ALL, blue)

ending_marker = 155720
addPauzeEvent(ending_marker + 0, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(ending_marker + 700, Effect.FLASH, KASTEN.ALL, yellow)
addPauzeEvent(ending_marker + 1400, Effect.FLASH, KASTEN.ALL, yellow)

# clear
addPauzeEvent(ending_marker + 1600, Effect.STATIC, KASTEN.ALL, clear)