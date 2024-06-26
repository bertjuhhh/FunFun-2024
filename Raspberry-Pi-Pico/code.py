import time
import board
import digitalio
import neopixel
import analogio

# LED strip configuration:
LED_COUNT = 10  # Number of LED pixels.
LED_PIN_BLUE = board.GP2  # GPIO pin connected to the Blue LED strip.
LED_PIN_BLUE_TWO = board.GP3  # GPIO pin connected to the second Blue LED strip.
POTENTIOMETER_PIN = board.GP26  # GPIO pin connected to the potentiometer for speed.
COLOR_POTENTIOMETER_PIN = board.GP27  # GPIO pin connected to the potentiometer for color.

# Create NeoPixel objects
ledsBlue = neopixel.NeoPixel(LED_PIN_BLUE, LED_COUNT, auto_write=False)
ledsBlueTwo = neopixel.NeoPixel(LED_PIN_BLUE_TWO, LED_COUNT, auto_write=False)

# Pulsating config
previousMillis = 0
interval = 5  # 12
brightness = 255
fadeAmount = -4
minBrightness = 20

# Chase light config
LED_ON_OFF_COUNT = 20
SPACING = 18
speed_pot = analogio.AnalogIn(POTENTIOMETER_PIN)  # Potentiometer input pin for speed
color_pot = analogio.AnalogIn(COLOR_POTENTIOMETER_PIN)  # Potentiometer input pin for color
offset = 0
movingUp = True

# Digital input pins
inputPin = digitalio.DigitalInOut(board.GP15)
inputPin.direction = digitalio.Direction.INPUT
inputPin.pull = digitalio.Pull.UP

inputPin1 = digitalio.DigitalInOut(board.GP14)
inputPin1.direction = digitalio.Direction.INPUT
inputPin1.pull = digitalio.Pull.UP

# Variables to manage state
chase_active = False
pulsate_active = False

def clearLEDs():
    for i in range(LED_COUNT):
        ledsBlue[i] = (0, 0, 0)
        ledsBlueTwo[i] = (0, 0, 0)
    ledsBlue.show()
    ledsBlueTwo.show()

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

    ledsBlue.show()
    ledsBlueTwo.show()
    time.sleep(speed / 100.0)  # Adjust speed using the potentiometer

def pulsateLEDs(color):
    global previousMillis, brightness, fadeAmount
    currentMillis = time.monotonic() * 1000
    if currentMillis - previousMillis >= interval:
        previousMillis = currentMillis
        brightness += fadeAmount

        if brightness <= minBrightness or brightness >= 255:
            fadeAmount = -fadeAmount

        for i in range(LED_COUNT):
            ledsBlue[i] = color
            ledsBlueTwo[i] = color

        ledsBlue.brightness = brightness / 255.0
        ledsBlueTwo.brightness = brightness / 255.0

        ledsBlue.show()
        ledsBlueTwo.show()

        print(f"Brightness: {brightness}, Color: {color}")

def main():
    global chase_active, pulsate_active
    while True:
        inputValue = not inputPin.value  # Active low: True when pressed
        inputValue1 = not inputPin1.value  # Active low: True when pressed

        if inputValue and not inputValue1:
            chase_active = True
            pulsate_active = False
        elif inputValue1 and not inputValue:
            chase_active = False
            pulsate_active = True
        elif inputValue and inputValue1:
            chase_active = False
            pulsate_active = False
        else:
            chase_active = False
            pulsate_active = False
            clearLEDs()

        # Read color potentiometer value and map to color wheel position
        color_value = color_pot.value
        color_position = int((color_value / 65535.0) * 255)
        color = color_wheel(color_position)

        if chase_active:
            pot_value = speed_pot.value
            speed = 0 + (pot_value / 65535.0) * 40  # Map potentiometer reading to a speed between 20 and 60
            print(f"Potentiometer Value: {pot_value}, Mapped Speed: {speed}, Color: {color}")
            ChaseLights(speed, color)
        elif pulsate_active:
            pulsateLEDs(color)

        time.sleep(0.01)

if __name__ == "__main__":
    main()