from lib.Ledkast import Ledkast
#from typing import Optional
from machine import Pin 
# Used for switching between the different LEDKASTS previewing them on the hoofdkast
POTENTIOMETER_PIN = 26

# Not used currently
COLOR_POTENTIOMETER_PIN = 27

# Serial monitor
UART_TX_PIN = 4
UART_RX_PIN = 5
UART_BAUDRATE = 9600

# Create Ledkast objects
#LEDKAST_1 = 0,10#Ledkast(board.GP0, 10) #is fout (geen board.gp gebruiken)
#LEDKAST_2 = 1,10#Ledkast(board.GP1, 10) #is fout (geen board.gp gebruiken)
#LEDKAST_3 = 2,10#Ledkast(board.GP2, 10) #is fout (geen board.gp gebruiken)
#LEDKAST_4 = 3,10#Ledkast(board.GP3, 10) #is fout (geen board.gp gebruiken)
LEDKAST_1 = Ledkast(pin=0, ledCount=10)  # weet niet of dit helemaal goed is
LEDKAST_2 = Ledkast(pin=1, ledCount=10)  # weet niet of dit helemaal goed is
LEDKAST_3 = Ledkast(pin=2, ledCount=10)  # weet niet of dit helemaal goed is
LEDKAST_4 = Ledkast(pin=3, ledCount=10)  # weet niet of dit helemaal goed is
# Indicators that are present on the hoofdkast
EXTERNAL_INDICATORS = Ledkast(pin=6, ledCount=10)# Ledkast(board.GP6, 10) ool checken

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
