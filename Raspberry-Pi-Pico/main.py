import time
from machine import Pin, ADC, UART
from config import getLedkast, getAllLedkastsExceptExternal, getAllLedkasts, UART_BAUDRATE, UART_TX_PIN, UART_RX_PIN, EXTERNAL_INDICATORS, POTENTIOMETER_PIN
from lib.Ledkast import Ledkast
from lib.Effect import Effect
import asyncio

# Initialize POT meter
pot = ADC(Pin(POTENTIOMETER_PIN))

# Initialize UART
uart = UART(1, baudrate=UART_BAUDRATE, tx=Pin(UART_TX_PIN), rx=Pin(UART_RX_PIN))

def validateData(data: str):
    return len(data.split("-")) == 4

async def startCommand(ledkast_name: str, effect: Effect):
    ledkast = getLedkast(ledkast_name)
    if ledkast:
        await ledkast.startEffect(effect=effect)
    else:
        print("⚠️ Invalid LEDKAST received. Skipping...")

async def startUpSequence():
    for kast in getAllLedkasts():
        await kast.showStartupEffect()

def showStatus():
    indicatorStrip = EXTERNAL_INDICATORS.strips
    ledkasten = getAllLedkastsExceptExternal()

    potValue = pot.read_u16() / 65535  # Normalize pot value
    selectedIndex = min(int(potValue * 4), len(ledkasten) - 1)
    ledkast = ledkasten[selectedIndex]

    # Clear all indicators first
    indicatorStrip.fill((0, 0, 0))

    # Set the selected LEDKAST indicator
    indicatorStrip[selectedIndex] = (255, 255, 255)

    # Preview the first 10 LEDs of the selected LEDKAST
    for i in range(4, 10):
        indicatorStrip[i] = ledkast.strips[i] if i < len(ledkast.strips) else (0, 0, 0)

    indicatorStrip.write()

def showError():
    EXTERNAL_INDICATORS.strips.fill((255, 0, 0))
    EXTERNAL_INDICATORS.strips.write()

async def uart_listener():
    buffer = ""
    while True:
        if uart.any():
            buffer += uart.read().decode()
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                line = line.strip()
                if validateData(line):
                    dmxEffect, ledkast, rgbColor, bpm = line.split("-")
                    effect = Effect(dmxEffect, bpm, rgbColor)
                    
                    if ledkast == "ALL":
                        for kast in getAllLedkastsExceptExternal():
                            await startCommand(kast.name, effect)
                    else:
                        await startCommand(ledkast, effect)
                else:
                    print(f"⚠️ Invalid data received. Skipping... {line}")
        await asyncio.sleep(0.1)

async def main():
    EXTERNAL_INDICATORS.strips.fill((0, 0, 0))
    EXTERNAL_INDICATORS.strips.write()
    print("🚀 Starting Raspberry Pi Pico...")
    await startUpSequence()
    print("🚀 Raspberry Pi Pico started successfully.")
    
    asyncio.create_task(uart_listener())

    while True:
        showStatus()
        await asyncio.sleep(0.2)

if __name__ == "__main__":
    asyncio.run(main())

