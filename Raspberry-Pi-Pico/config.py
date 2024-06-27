import board
from lib.Ledkast import Ledkast
from typing import Optional

POTENTIOMETER_PIN = board.GP26
COLOR_POTENTIOMETER_PIN = board.GP27
INPUT_PIN = board.GP15
INPUT_PIN1 = board.GP14

# Create Ledkast objects
LEDKAST_1 = Ledkast(board.GP2, 10)
LEDKAST_2 = Ledkast(board.GP3, 10)
LEDKAST_3 = Ledkast(board.GP4, 10) # Check this
LEDKAST_4 = Ledkast(board.GP5, 10) # Check this
EXTERNAL_INDICATORS = Ledkast(board.GP2, 10)

def getLedkast(group: str) -> Optional[Ledkast]:
    if group == "LEDKAST_1":
        return LEDKAST_1
    elif group == "LEDKAST_2":
        return LEDKAST_2
    elif group == "LEDKAST_3":
        return LEDKAST_3
    elif group == "LEDKAST_4":
        return LEDKAST_4
    else:
        return None
    
def getAllLedkasts() -> list[Ledkast]:
    return [LEDKAST_1, LEDKAST_2, LEDKAST_3, LEDKAST_4, EXTERNAL_INDICATORS]