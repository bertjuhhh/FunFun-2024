from eventLoop import addEventToLoop
from lib.Effects import Effect
from lib.Colors import clear, lime, yellow, gold, blue, pink, yellow, red
from lib.Groups import Groups

partyLoop = []

startMarker = 1240

addEventToLoop(partyLoop, startMarker, Effect.PULSATE, Groups.ALL, lime)

buildupMarker = 21540

addEventToLoop(partyLoop, buildupMarker, Effect.PULSATE, blue)

climaxMarker = 31570

addEventToLoop(partyLoop, climaxMarker, Effect.BPMFLASH, Groups.LEDKAST_1, blue)
addEventToLoop(partyLoop, climaxMarker, Effect.BPMFLASH, Groups.LEDKAST_2, pink)
addEventToLoop(partyLoop, climaxMarker, Effect.BPMFLASH, Groups.LEDKAST_3, yellow)
addEventToLoop(partyLoop, climaxMarker, Effect.BPMFLASH, Groups.LEDKAST_4, lime)

beforeBeatMarker = 55750
beatMarker = 56660

addEventToLoop(partyLoop, beforeBeatMarker, Effect.FLASH, Groups.ALL, red)

addEventToLoop(partyLoop, beatMarker, Effect.BPMFLASH, Groups.LEDKAST_1, red)
addEventToLoop(partyLoop, beatMarker, Effect.CHASE, Groups.LEDKAST_2, red)
addEventToLoop(partyLoop, beatMarker, Effect.PULSATE, Groups.LEDKAST_3, red)
addEventToLoop(partyLoop, beatMarker, Effect.CHASE, Groups.LEDKAST_3, red)