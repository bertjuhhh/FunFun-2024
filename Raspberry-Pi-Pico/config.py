from lib.Ledkast import Ledkast
# Used for switching between the different LEDKASTS previewing them on the hoofdkast
POTENTIOMETER_PIN = 27

# Not used currently
COLOR_POTENTIOMETER_PIN = 26

# Serial monitor
UART_TX_PIN = 4
UART_RX_PIN = 5
UART_BAUDRATE = 9600

# LEDKAST_1 = Ledkast(pin=0, ledCount=150, name="LEDKAST_1")  
# LEDKAST_2 = Ledkast(pin=2, ledCount=150, name="LEDKAST_2")  
LEDKAST_3 = Ledkast(pin=12, ledCount=300, name="LEDKAST_3")  
LEDKAST_4 = Ledkast(pin=14, ledCount=300, name="LEDKAST_4") 

# Indicators that are present on the hoofdkast
EXTERNAL_INDICATORS = Ledkast(pin=16, ledCount=10 , name="EXTERNAL_INDICATORS")# Ledkast(board.GP6, 10) ool checken

def getLedkast(group: str):
    if group == "None":
        return None
    elif group == "LEDKAST_2":
        return None
    elif group == "LEDKAST_3":
        return LEDKAST_3
    elif group == "LEDKAST_4":
        return LEDKAST_4
    elif group == "EXTERNAL_INDICATORS":
        return EXTERNAL_INDICATORS
    else:
        return None
    
def getAllLedkasts() -> list[Ledkast]:
    return [None, None, LEDKAST_3, LEDKAST_4, None, None, EXTERNAL_INDICATORS]

def getAllLedkastsExceptExternal() -> list[Ledkast]:
    return [None, None, LEDKAST_3, LEDKAST_4]
