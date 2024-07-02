import time
from machine import Pin, ADC, UART
from config import getLedkast, getAllLedkastsExceptExternal, getAllLedkasts, UART_BAUDRATE, UART_TX_PIN, UART_RX_PIN, EXTERNAL_INDICATORS, POTENTIOMETER_PIN

from lib.Ledkast import Ledkast
from lib.Effect import Effect


# Initialize POT meter
pot = ADC(Pin(POTENTIOMETER_PIN))

# Initialize UART (UART0 in Raspberry Pi Pico)
uart = UART(1, baudrate=UART_BAUDRATE, tx=Pin(UART_TX_PIN), rx=Pin(UART_RX_PIN))

def validateData(data: str):
    dataArray = data.split("-")
    
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
# When rotating the POT meter, it switches between the different LEDKASTS, previewing them on the hoofdkast
# We have four groups so the pot meter is divided into four sections
def showStatus():
    indicatorStrip = EXTERNAL_INDICATORS.strips
    ledkasten = getAllLedkastsExceptExternal()
    
    potValue = pot.read_u16()
    potValue = potValue / 65535  # Normalize pot value to range 0-1
    
    selectedIndex = 0
    print(f"Pot value: {potValue}")
    
    # Determine the selected LEDKAST based on the pot value
    if potValue < 0.25:
        selectedIndex = 0
    elif potValue < 0.5:
        selectedIndex = 1
    elif potValue < 0.75:
        selectedIndex = 2
    else:
        selectedIndex = 3
    
    ledkast = ledkasten[selectedIndex]
    
    # Represent the selected LEDKAST index in binary on the first two LEDs
    binary = "{0:b}".format(selectedIndex).zfill(2)
    
    for i in range(2):
        indicatorStrip[i] = (255, 255, 255) if binary[i] == "1" else (0, 0, 0)
    
    # Preview the first 10 LEDs of the selected LEDKAST on the indicator strip
    for i in range(2, 10):
        indicatorStrip[i] = ledkast.strips[i] if i < len(ledkast.strips) else (0, 0, 0)
        
    indicatorStrip.write()

    
def showError():
    indicatorStrip = EXTERNAL_INDICATORS.strips
    
    for i in range(10):
        indicatorStrip[i] = (0, 0, 0)
    
    for i in range(10):
        indicatorStrip[i] = (255, 0, 0)
            
    indicatorStrip.write()
    

def main():    
    print("🚀 Starting Raspberry Pi Pico...")
    startUpSequence()

    while True:
        if uart.any():
            try:
                # convert the data to a string
                # Expected format: `{START/STOP}-{LEDKAST}-{DMX EFFECT}-{RGB COLOR}`
                data = uart.readline().decode().strip()
                
                
                # Validate the data
                if (not validateData(data)):
                    print(f"⚠️ Invalid data received. Skipping... {data}")
                    continue
                
                (startOrSop, ledkast, dmxEffect, rgbColor) = data.split("-")
                effect = Effect(dmxEffect, rgbColor)
                
                if startOrSop.upper() == "START":
                    startCommand(ledkast, effect)
                else:
                    stopCommand(ledkast)
                    
                showStatus()
                
            except Exception as e:
                print(f"⚠️ An error occurred. Skipping... {e}")
                showError()
                
        time.sleep(0.1)


if __name__ == "__main__":
    main()
