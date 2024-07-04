import time
from machine import Pin, ADC, UART
from config import getLedkast, getAllLedkastsExceptExternal, getAllLedkasts, UART_BAUDRATE, UART_TX_PIN, UART_RX_PIN, EXTERNAL_INDICATORS, POTENTIOMETER_PIN
from lib.Ledkast import Ledkast
from lib.Effect import Effect
import asyncio

# Initialize POT meter
pot = ADC(Pin(POTENTIOMETER_PIN))

# Initialize UART (UART0 in Raspberry Pi Pico)
uart = UART(1, baudrate=UART_BAUDRATE, tx=Pin(UART_TX_PIN), rx=Pin(UART_RX_PIN))

def validateData(data: str):
    dataArray = data.split("-")
    if len(dataArray) != 3:
        return False
    return True

async def startCommand(ledkast_name: str, effect: Effect):
    ledkast: Ledkast = getLedkast(ledkast_name)
    
    # No LEDKAST found
    if ledkast is None:
        print("⚠️ Invalid LEDKAST received. Skipping...")
        return
    
    await ledkast.startEffect(effect=effect)
    
async def startUpSequence():
    kasten = getAllLedkasts()
    for kast in kasten:
        await kast.showStartupEffect()

# This displays the status on the external indicators in the following:
# When rotating the POT meter, it switches between the different LEDKASTS, previewing them on the hoofdkast
# We have four groups so the pot meter is divided into four sections
def showStatus():
    indicatorStrip = EXTERNAL_INDICATORS.strips
    ledkasten = getAllLedkastsExceptExternal()
    
    potValue = pot.read_u16()
    potValue = potValue / 65535  # Normalize pot value to range 0-1
    
    selectedIndex = 0
    
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
    
    for i in range(10):
        indicatorStrip[i] = (0, 0, 0)
    
    indicatorStrip[selectedIndex] = (255, 255, 255) 
    
    # Preview the first 10 LEDs of the selected LEDKAST on the indicator strip
    for i in range(4, 10):
        indicatorStrip[i] = ledkast.strips[i] if i < len(ledkast.strips) else (0, 0, 0)
        
    indicatorStrip.write()

    
def showError():
    indicatorStrip = EXTERNAL_INDICATORS.strips
    
    for i in range(10):
        indicatorStrip[i] = (0, 0, 0)
    
    for i in range(10):
        indicatorStrip[i] = (255, 0, 0)
            
    indicatorStrip.write()

async def uart_listener():
    buffer = ""
    while True:
        if uart.any():
            try:
                buffer += uart.read().decode()
                if "\n" in buffer:
                    data, buffer = buffer.split("\n", 1)  # Get the first complete command and keep the rest
                    data = data.strip()
                    if not validateData(data):
                        print(f"⚠️ Invalid data received. Skipping... {data}")
                        continue
                    
                    print(f"📡 Received data: {data}")

                    dmxEffect, ledkast, rgbColor = data.split("-")
                    effect = Effect(dmxEffect, rgbColor)
                    
                    await startCommand(ledkast, effect)
            except Exception as e:
                print(f"⚠️ An error occurred. Skipping... {e}")
                showError()
        await asyncio.sleep(0.1)  # Small delay to prevent busy waiting

async def main():
    indicatorStrip = EXTERNAL_INDICATORS.strips
    
    for i in range(10):
        indicatorStrip[i] = (0, 0, 0)
        
    indicatorStrip.write()
    print("🚀 Starting Raspberry Pi Pico...")
    await startUpSequence()
    print("🚀 Raspberry Pi Pico started successfully.")
    
    # Start the UART listener task
    uart_task = asyncio.create_task(uart_listener())

    # Keep the main function running indefinitely
    while True:
        showStatus()
        await asyncio.sleep(0.07)  # Update status at regular intervals

if __name__ == "__main__":
    asyncio.run(main())
