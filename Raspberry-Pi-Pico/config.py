from lib.Ledkast import Ledkast
from typing import Optional

# Used for switching between the different LEDKASTS previewing them on the hoofdkast
POTENTIOMETER_PIN = board.GP26

# Not used currently
COLOR_POTENTIOMETER_PIN = board.GP27

# Serial monitor
UART_TX_PIN = 4
UART_RX_PIN = 5
UART_BAUDRATE = 9600

# Create Ledkast objects
LEDKAST_1 = Ledkast(board.GP0, 10)
LEDKAST_2 = Ledkast(board.GP1, 10)
LEDKAST_3 = Ledkast(board.GP2, 10) # Check this
LEDKAST_4 = Ledkast(board.GP3, 10) # Check this

# Indicators that are present on the hoofdkast
EXTERNAL_INDICATORS = Ledkast(board.GP6, 10)

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

def getAllLedkastsExceptExternal() -> list[Ledkast]:
    return [LEDKAST_1, LEDKAST_2, LEDKAST_3, LEDKAST_4]