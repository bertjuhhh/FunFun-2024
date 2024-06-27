import time
from machine import Pin, ADC, UART
from config import getLedkast, getAllLedkasts, UART_BAUDRATE, UART_TX_PIN, UART_RX_PIN

from lib.Ledkast import Ledkast
from lib.Effect import Effect

# Initialize UART (UART0 in Raspberry Pi Pico)
uart = UART(1, baudrate=UART_BAUDRATE, tx=Pin(UART_TX_PIN), rx=Pin(UART_RX_PIN))

def validateData(data: str):
    dataArray = data.split("_")
    
    if len(dataArray) != 4:
        return False
    
    if dataArray[0] not in ["START", "STOP"]:
        return False
    
    return True

def startCommand(ledkast: str, effect: Effect):
    ledkast: Ledkast = getLedkast(ledkast)
    
    # No LEDKAST found
    if ledkast is None:
        print("⚠️ Invalid LEDKAST received. Skipping...")
        return
    
    ledkast.startEffect(effect=effect)
    
def stopCommand(ledkast: str):
    ledkast: Ledkast = getLedkast(ledkast)
    
    # No LEDKAST found
    if ledkast is None:
        print("⚠️ Invalid LEDKAST received. Skipping...")
        return
    
    ledkast.clearLEDs()
    
def startUpSequence():
    kasten = getAllLedkasts()
    
    for kast in kasten:
        kast.showStartupEffect()
    

def main():
    global chase_active, pulsate_active
    
    print("🚀 Starting Raspberry Pi Pico...")
    startUpSequence()
    

    while True:
        if uart.any():
            # convert the data to a string
            # Expected format: `{START/STOP}_{LEDKAST}_{DMX EFFECT}_{RGB COLOR}`
            data = uart.readline().decode().strip()
            
            
            # Validate the data
            if (not validateData(data)):
                print("⚠️ Invalid data received. Skipping...")
                continue
            
            (startOrSop, ledkast, dmxEffect, rgbColor) = data.split("_")
            effect = Effect(dmxEffect, rgbColor)
            
            if startOrSop == "START":
                startCommand(ledkast, effect)
            else:
                stopCommand(ledkast)


if __name__ == "__main__":
    main()
