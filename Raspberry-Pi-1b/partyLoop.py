from eventLoop import addToGroup
from lib.Groups import outside_group
from lib.Effects import Effect
from lib.Colors import clear, lime, yellow, gold, blue, pink, yellow, red

partyLoop = []

startMarker = 1240

addToGroup(partyLoop, startMarker, Effect.PULSATE, outside_group, lime)

buildupMarker = 21540

addToGroup(partyLoop, buildupMarker, Effect.PULSATE, blue)

climaxMarker = 31570

addToGroup(partyLoop, climaxMarker, Effect.BPMFLASH, outside_group, pink)

beforeBeatMarker = 55750
beatMarker = 56660

addToGroup(partyLoop, beforeBeatMarker, Effect.FLASH, outside_group, red)

addToGroup(partyLoop, beatMarker, Effect.PULSATE, outside_group, red)
