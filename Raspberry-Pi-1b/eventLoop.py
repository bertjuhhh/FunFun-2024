from lib.TimedEvent import TimedEvent
from lib.Effects import Effect
from lib.Kasten import KASTEN
from lib.Groups import outside_group, internal_indicators
from lib.Colors import blue, clear, lime, yellow, gold, dark_orange, red

# typed array
mainLoop: list[TimedEvent] = []
pauzeLoop: list[TimedEvent] = []
discoLoop: list[TimedEvent] = []

def addToGroup(loop, start, effect: Effect, group, color = None):
    for kast in group:
        loop.append(TimedEvent(start=start, effect=effect, group=kast, color=color))
    
def addSingle(loop, start, effect, kast, color):
    loop.append(TimedEvent(start=start, effect=effect, group=kast, color=color))
    
def addPauzeEvent(start, effect: Effect, group, color = None):
    addToGroup(pauzeLoop, start, effect, [group], color)
    
def clearAll(loop):
    group1 = TimedEvent(start=0, effect=Effect.STATIC, group=outside_group, color=clear)
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
# EXTERNAL
addToGroup(mainLoop, 0, Effect.SPARKLE, outside_group, lime)
addToGroup(mainLoop, 28000, Effect.SPARKLE, outside_group, yellow)
addToGroup(mainLoop, 45000, Effect.PULSATE, outside_group, yellow)

# BEWEGERS INDICATOREN
addToGroup(mainLoop, 0, Effect.STATIC, internal_indicators, red)
addToGroup(mainLoop, 24000, Effect.STATIC, internal_indicators, dark_orange)
addToGroup(mainLoop, 27000, Effect.STATIC, internal_indicators, lime)

addToGroup(mainLoop, 42000, Effect.STATIC, internal_indicators, dark_orange)
addToGroup(mainLoop, 45000, Effect.STATIC, internal_indicators, lime)

addToGroup(mainLoop, 67000, Effect.STATIC, internal_indicators, dark_orange)
addToGroup(mainLoop, 70000, Effect.STATIC, internal_indicators, lime)

addToGroup(mainLoop, 87000, Effect.STATIC, internal_indicators, dark_orange)
addToGroup(mainLoop, 90000, Effect.STATIC, internal_indicators, red)

# EUROPAPA
addToGroup(pauzeLoop, 0, Effect.CHASE, outside_group, dark_orange)
addToGroup(pauzeLoop, 13200, Effect.FLASH, outside_group, blue)
addToGroup(pauzeLoop, 14200, Effect.PULSATE, outside_group, yellow)
addToGroup(pauzeLoop, 16800, Effect.FLASH, outside_group, blue)
addToGroup(pauzeLoop, 17200, Effect.THEATER_CHASE_RAINBOW, outside_group, blue)
addToGroup(pauzeLoop, 18200, Effect.FLASH, outside_group, blue)
addToGroup(pauzeLoop, 18700, Effect.FLASH, outside_group, blue)
addToGroup(pauzeLoop, 19500, Effect.FLASH, outside_group, blue)
addToGroup(pauzeLoop, 25230, Effect.BPMFLASH, outside_group, blue)
addToGroup(pauzeLoop, 43290, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, 44750, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, 46000, Effect.FLASH, outside_group, yellow)

# verse marker
chorus1_start = 49140
addToGroup(pauzeLoop, chorus1_start, Effect.BPMFLASH, outside_group, blue)

addToGroup(pauzeLoop, chorus1_start + 3560, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, chorus1_start + 3920, Effect.FLASH, outside_group, yellow)

addToGroup(pauzeLoop, chorus1_start + 5240, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, chorus1_start + 5680, Effect.FLASH, outside_group, yellow)


addToGroup(pauzeLoop, chorus1_start + 5900, Effect.BPMFLASH, outside_group, blue)


addToGroup(pauzeLoop, chorus1_start + 9640, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, chorus1_start + 10040, Effect.FLASH, outside_group, yellow)

addToGroup(pauzeLoop, chorus1_start + 11160, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, chorus1_start + 11510, Effect.FLASH, outside_group, yellow)

addToGroup(pauzeLoop, chorus1_start + 12500, Effect.BPMFLASH, outside_group, blue)

addToGroup(pauzeLoop, chorus1_start + 17380, Effect.FLASH, outside_group, yellow)

addToGroup(pauzeLoop, chorus1_start + 18200, Effect.BPMFLASH, outside_group, blue)

# EU, RO, PA
addToGroup(pauzeLoop, chorus1_start + 21130, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, chorus1_start + 21830, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, chorus1_start + 22590, Effect.FLASH, outside_group, yellow)

addToGroup(pauzeLoop, chorus1_start + 23600, Effect.FLASH, outside_group, yellow)

addToGroup(pauzeLoop, chorus1_start + 25000, Effect.BPMFLASH, outside_group, blue)

verse2_marker = 73120

addToGroup(pauzeLoop, verse2_marker + 0, Effect.BPMFLASH, outside_group, blue)


chorus2_marker = 97190
addToGroup(pauzeLoop, chorus2_marker, Effect.BPMFLASH, outside_group, blue)

addToGroup(pauzeLoop, chorus2_marker + 3560, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, chorus2_marker + 3920, Effect.FLASH, outside_group, yellow)

addToGroup(pauzeLoop, chorus2_marker + 5240, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, chorus2_marker + 5680, Effect.FLASH, outside_group, yellow)


addToGroup(pauzeLoop, chorus2_marker + 5900, Effect.BPMFLASH, outside_group, blue)


addToGroup(pauzeLoop, chorus2_marker + 9640, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, chorus2_marker + 10040, Effect.FLASH, outside_group, yellow)

addToGroup(pauzeLoop, chorus2_marker + 11160, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, chorus2_marker + 11510, Effect.FLASH, outside_group, yellow)

addToGroup(pauzeLoop, chorus2_marker + 12500, Effect.BPMFLASH, outside_group, blue)

# EU, RO, PA
addToGroup(pauzeLoop, chorus2_marker + 21130, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, chorus2_marker + 21830, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, chorus2_marker + 22590, Effect.FLASH, outside_group, yellow)

addToGroup(pauzeLoop, 120000, Effect.PULSATE, outside_group, yellow)
addToGroup(pauzeLoop, 133050, Effect.FLASH, outside_group, yellow)

addToGroup(pauzeLoop, 135100, Effect.BPMFLASH, outside_group, blue)
addToGroup(pauzeLoop, 146720, Effect.BPMFLASH, outside_group, yellow)

addToGroup(pauzeLoop, 14967, Effect.BPMFLASH, outside_group, blue)

addToGroup(pauzeLoop, 152010, Effect.FLASH, outside_group, yellow)

addToGroup(pauzeLoop, 153070, Effect.BPMFLASH, outside_group, blue)

ending_marker = 155720
addToGroup(pauzeLoop, ending_marker + 0, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, ending_marker + 700, Effect.FLASH, outside_group, yellow)
addToGroup(pauzeLoop, ending_marker + 1400, Effect.FLASH, outside_group, yellow)

# clear
addToGroup(pauzeLoop, ending_marker + 1600, Effect.STATIC, outside_group, clear)