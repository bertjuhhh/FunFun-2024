import time
from machine import Pin, ADC, UART
from config import getLedkast, getAllLedkasts, UART_BAUDRATE, UART_TX_PIN, UART_RX_PIN, EXTERNAL_INDICATORS

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
    
# This displays the status on the external indicators in the following:
# The led strip has 10 leds, 2 for each group. 
# The first led displays if a group ios active in green, the second mimicks the color of the group.
def showStatus():
    indicatorStrip = EXTERNAL_INDICATORS.strips
    
    for i in range(10):
        indicatorStrip[i] = (0, 0, 0)
    
    for i, kast in enumerate(getAllLedkasts()):
        if kast.isActive:
            indicatorStrip[i * 2] = (0, 255, 0)
            indicatorStrip[i * 2 + 1] = kast.strips[0]
            
    indicatorStrip.show()
    
def showError():
    indicatorStrip = EXTERNAL_INDICATORS.strips
    
    for i in range(10):
        indicatorStrip[i] = (0, 0, 0)
    
    for i in range(10):
        indicatorStrip[i] = (255, 0, 0)
            
    indicatorStrip.show()
    

def main():    
    print("🚀 Starting Raspberry Pi Pico...")
    startUpSequence()

    while True:
        if uart.any():
            try:
                # convert the data to a string
                # Expected format: `{START/STOP}_{LEDKAST}_{DMX EFFECT}_{RGB COLOR}`
                data = uart.readline().decode().strip()
                
                
                # Validate the data
                if (not validateData(data)):
                    print("⚠️ Invalid data received. Skipping...")
                    continue
                
                (startOrSop, ledkast, dmxEffect, rgbColor) = data.split("_")
                effect = Effect(dmxEffect, rgbColor)
                
                if startOrSop.upper() == "START":
                    startCommand(ledkast, effect)
                else:
                    stopCommand(ledkast)
                    
                showStatus()
                
            except Exception as e:
                print("⚠️ An error occurred. Skipping...")
                showError()
                
        time.sleep(0.1)


if __name__ == "__main__":
    main()
