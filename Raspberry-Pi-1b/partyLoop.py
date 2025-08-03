from eventLoop import addToGroup
from lib.Groups import windroos
from lib.Effects import Effect
from lib.Colors import clear, lime, yellow, gold, blue, pink, yellow, red

partyLoop = []

startMarker = 1240

addToGroup(partyLoop, startMarker, Effect.PULSATE, windroos, lime)

buildupMarker = 21540

addToGroup(partyLoop, buildupMarker, Effect.PULSATE, windroos, blue)

climaxMarker = 31570

addToGroup(partyLoop, climaxMarker, Effect.BPMFLASH, windroos, pink)

beforeBeatMarker = 55750
beatMarker = 56660

addToGroup(partyLoop, beforeBeatMarker, Effect.FLASH, windroos, red)

addToGroup(partyLoop, beatMarker, Effect.PULSATE, windroos, red)
