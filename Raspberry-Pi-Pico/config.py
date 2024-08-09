from lib.Ledkast import Ledkast
# Used for switching between the different LEDKASTS previewing them on the hoofdkast
POTENTIOMETER_PIN = 27

# Not used currently
COLOR_POTENTIOMETER_PIN = 26

# Serial monitor
UART_TX_PIN = 4
UART_RX_PIN = 5
UART_BAUDRATE = 9600

LEDKAST_1 = Ledkast(pin=0, ledCount=150, name="LEDKAST_1") 
LEDKAST_1b = Ledkast(pin=1, ledCount=10, name="LEDKAST_1b") 
LEDKAST_2 = Ledkast(pin=2, ledCount=150, name="LEDKAST_2") 
LEDKAST_2b = Ledkast(pin=3, ledCount=10, name="LEDKAST_2b") 
LEDKAST_3 = Ledkast(pin=12, ledCount=150, name="LEDKAST_3") 
LEDKAST_3b = Ledkast(pin=13, ledCount=10, name="LEDKAST_3b") 
LEDKAST_4 = Ledkast(pin=14, ledCount=150, name="LEDKAST_4") 
LEDKAST_4b = Ledkast(pin=15, ledCount=10, name="LEDKAST_4b")

# Indicators that are present on the hoofdkast
EXTERNAL_INDICATORS = Ledkast(pin=16, ledCount=10 , name="EXTERNAL_INDICATORS")# Ledkast(board.GP6, 10) ool checken

def getLedkast(group: str):
    if group == "LEDKAST_1":
        return LEDKAST_1
    elif group == "LEDKAST_2":
        return LEDKAST_2
    elif group == "LEDKAST_3":
        return LEDKAST_3
    elif group == "LEDKAST_4":
        return LEDKAST_4
    elif group == "LEDKAST_1b":
        return LEDKAST_1
    elif group == "LEDKAST_2b":
        return LEDKAST_2
    elif group == "LEDKAST_3b":
        return LEDKAST_3
    elif group == "LEDKAST_4b":
        return LEDKAST_4
    elif group == "EXTERNAL_INDICATORS":
        return EXTERNAL_INDICATORS
    else:
        return None
    
def getAllLedkasts() -> list[Ledkast]:
    return [LEDKAST_1, LEDKAST_2, LEDKAST_3, LEDKAST_4, LEDKAST_1b, LEDKAST_2b, LEDKAST_3b, LEDKAST_4b, EXTERNAL_INDICATORS]

def getAllLedkastsExceptExternal() -> list[Ledkast]:
    return [LEDKAST_1, LEDKAST_2, LEDKAST_3, LEDKAST_4, LEDKAST_1b, LEDKAST_2b, LEDKAST_3b, LEDKAST_4b]
