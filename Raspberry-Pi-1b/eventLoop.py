from lib.TimedEvent import TimedEvent
from lib.Effects import Effect
from lib.Groups import outside_group
from lib.Colors import blue, clear, lime, yellow, gold, dark_orange, red, green

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
    
# Currently, only STATIC, FLASH and PULSATE are supported
# Times in milliseconds    
# 0 = infinite
# EXTERNAL
# addToGroup(mainLoop, 0, Effect.STATIC, outside_group, red)
# addToGroup(mainLoop, 3000, Effect.STATIC, outside_group, blue)
# addToGroup(mainLoop, 6000, Effect.STATIC, outside_group, green)
# addToGroup(mainLoop, 9000, Effect.STATIC, outside_group, red)
# addToGroup(mainLoop, 12000, Effect.STATIC, outside_group, blue)
# addToGroup(mainLoop, 15000, Effect.STATIC, outside_group, green)
# addToGroup(mainLoop, 18000, Effect.STATIC, outside_group, red)
# addToGroup(mainLoop, 21000, Effect.STATIC, outside_group, blue)
# addToGroup(mainLoop, 24000, Effect.STATIC, outside_group, green)
# addToGroup(mainLoop, 27000, Effect.STATIC, outside_group, red)
# addToGroup(mainLoop, 30000, Effect.STATIC, outside_group, blue)
# addToGroup(mainLoop, 33000, Effect.STATIC, outside_group, green)
# addToGroup(mainLoop, 36000, Effect.STATIC, outside_group, red)
# addToGroup(mainLoop, 39000, Effect.STATIC, outside_group, blue)
# addToGroup(mainLoop, 42000, Effect.STATIC, outside_group, green)
# addToGroup(mainLoop, 45000, Effect.STATIC, outside_group, red)
# addToGroup(mainLoop, 48000, Effect.STATIC, outside_group, blue)
# addToGroup(mainLoop, 51000, Effect.STATIC, outside_group, green)
# addToGroup(mainLoop, 54000, Effect.STATIC, outside_group, red)
# addToGroup(mainLoop, 57000, Effect.STATIC, outside_group, blue)
# addToGroup(mainLoop, 60000, Effect.STATIC, outside_group, green)   
# addToGroup(mainLoop, 63000, Effect.STATIC, outside_group, red)
# addToGroup(mainLoop, 66000, Effect.STATIC, outside_group, blue)
# addToGroup(mainLoop, 69000, Effect.STATIC, outside_group, green)
# addToGroup(mainLoop, 72000, Effect.STATIC, outside_group, red)
# addToGroup(mainLoop, 75000, Effect.STATIC, outside_group, blue)
# addToGroup(mainLoop, 78000, Effect.STATIC, outside_group, green)
# addToGroup(mainLoop, 81000, Effect.STATIC, outside_group, red)
# addToGroup(mainLoop, 84000, Effect.STATIC, outside_group, blue)
# addToGroup(mainLoop, 87000, Effect.STATIC, outside_group, green)
# addToGroup(mainLoop, 90000, Effect.STATIC, outside_group, red)


addToGroup(mainLoop, 0, Effect.SPARKLE, outside_group, lime)
addToGroup(mainLoop, 25000, Effect.FLASH, outside_group, lime)
addToGroup(mainLoop, 28000, Effect.SPARKLE, outside_group, yellow)
addToGroup(mainLoop, 45000, Effect.FLASH, outside_group, yellow)
addToGroup(mainLoop, 48000, Effect.CHASE, outside_group, yellow)
addToGroup(mainLoop, 87000, Effect.FLASH, outside_group, lime)
addToGroup(mainLoop, 90000, Effect.SPARKLE, outside_group, lime)


# PAUZE
addToGroup(pauzeLoop, 0, Effect.SPARKLE, outside_group, lime)