import time
from machine import Pin, ADC
import neopixel

# LED strip configuration:
LED_COUNT = 10
LED_PIN_BLUE = 2  # GP2
LED_PIN_BLUE_TWO = 3  # GP3

# Create NeoPixel objects
ledsBlue = neopixel.NeoPixel(Pin(LED_PIN_BLUE), LED_COUNT)
ledsBlueTwo = neopixel.NeoPixel(Pin(LED_PIN_BLUE_TWO), LED_COUNT)

# Pulsating config
previousMillis = 0.1
brightness = 1
fadeAmount = 10

# Chase light config
LED_ON_OFF_COUNT = 20
SPACING = 18
speed_pot = ADC(Pin(26))  # GP26
color_pot = ADC(Pin(27))  # GP27
offset = 0
movingUp = True

# Variables to manage state
chase_active = False
pulsate_active = False

# Initialize UART (UART0 in Raspberry Pi Pico)
uart = machine.UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

def clearLEDs():
    global ledsBlue, ledsBlueTwo
    for i in range(LED_COUNT):
        ledsBlue[i] = (0, 0, 0)
        ledsBlueTwo[i] = (0, 0, 0)
    ledsBlue.write()
    ledsBlueTwo.write()

def color_wheel(position):
    """Generate color based on a position from 0 to 255."""
    if position < 85:
        return (int(position * 3), int(255 - position * 3), 0)
    elif position < 170:
        position -= 85
        return (int(255 - position * 3), 0, int(position * 3))
    else:
        position -= 170
        return (0, int(position * 3), int(255 - position * 3))

def ChaseLights(speed, color):
    global offset, movingUp
    brightnessLevels = [20, 20, 75, 100, 150, 180, 255, 255, 255, 180, 150, 100, 75, 20, 20]

    # Turn off all LEDs
    for i in range(LED_COUNT):
        ledsBlue[i] = (0, 0, 0)
        ledsBlueTwo[i] = (0, 0, 0)

    # Turn on the specified number of LEDs
    for i in range(LED_COUNT):
        for j in range(LED_ON_OFF_COUNT):
            brightness = brightnessLevels[j % len(brightnessLevels)]
            if (i + j + offset) < LED_COUNT:
                ledsBlue[i + j + offset] = color
                ledsBlueTwo[i + j + offset] = color

    if movingUp:
        offset += 1
        if offset >= LED_ON_OFF_COUNT:
            movingUp = False
    else:
        offset -= 1
        if offset <= 0:
            movingUp = True

    ledsBlue.write()
    ledsBlueTwo.write()
    time.sleep(speed / 100.0)

def pulsateLEDs(color, interval):
    global previousMillis, brightness, fadeAmount
    currentMillis = time.ticks_ms()
    if currentMillis - previousMillis >= interval:
        previousMillis = currentMillis
        brightness += fadeAmount

        if brightness <= 10 or brightness >= 255:
            fadeAmount = -fadeAmount

        scaled_brightness = brightness / 255.10

        for i in range(LED_COUNT):
            # Scale color intensity by brightness
            scaled_color = tuple(int(channel * scaled_brightness) for channel in color)
            ledsBlue[i] = scaled_color
            ledsBlueTwo[i] = scaled_color

        ledsBlue.write()
        ledsBlueTwo.write()

        print("Brightness: {}, Interval: {}, Color: {}".format(brightness, interval, color))

def setAllLEDsRed():
    global ledsBlue, ledsBlueTwo
    for i in range(LED_COUNT):
        ledsBlue[i] = (255, 0, 0)
        ledsBlueTwo[i] = (255, 0, 0)
    ledsBlue.write()
    ledsBlueTwo.write()

def main():
    global chase_active, pulsate_active

    print("Setting all LEDs to red at the start.")
    setAllLEDsRed()

    while True:
        # Check if there's data available
        if uart.any():
            data = uart.read(4)  # Read up to 4 bytes of data

            # Process received data
            if data[0] == ord('c'):
                chase_active = True
                pulsate_active = False
                print("Chase mode activated.")
            elif data[0] == ord('p'):
                chase_active = False
                pulsate_active = True
                print("Pulsate mode activated.")
            elif data[0] == ord('b'):
                chase_active = False
                pulsate_active = False
                print("Both modes deactivated.")
            elif data[0] == ord('e'):
                chase_active = False
                pulsate_active = False
                clearLEDs()
                print("LEDs cleared.")

        # Read color potentiometer value and map to color wheel position
        color_value = color_pot.read_u16()
        color_position = int((color_value / 65535.0) * 255)
        color = color_wheel(color_position)

        if chase_active:
            pot_value = speed_pot.read_u16()
            speed = 0 + (pot_value / 65535.0) * 40
            print("Potentiometer Value: {}, Mapped Speed: {}, Color: {}".format(pot_value, speed, color))
            ChaseLights(speed, color)
        elif pulsate_active:
            pot_value = speed_pot.read_u16()
            interval = int(1 + (pot_value / 65535.0) * 20)  # Mapping potentiometer to interval 1ms to 21ms
            pulsateLEDs(color, interval)

        time.sleep(0.01)

if __name__ == "__main__":
    main()
