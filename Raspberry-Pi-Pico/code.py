import time
import board
import digitalio
import analogio
from config import LED_COUNT, POTENTIOMETER_PIN, COLOR_POTENTIOMETER_PIN, INPUT_PIN, INPUT_PIN1
from utils.led_utils import clearLEDs, color_wheel
from effects.chase_lights import ChaseLights
from effects.pulsate_leds import pulsateLEDs

# Initialize potentiometers
speed_pot = analogio.AnalogIn(POTENTIOMETER_PIN)
color_pot = analogio.AnalogIn(COLOR_POTENTIOMETER_PIN)

# Initialize input pins
inputPin = digitalio.DigitalInOut(INPUT_PIN)
inputPin.direction = digitalio.Direction.INPUT
inputPin.pull = digitalio.Pull.UP

inputPin1 = digitalio.DigitalInOut(INPUT_PIN1)
inputPin1.direction = digitalio.Direction.INPUT
inputPin1.pull = digitalio.Pull.UP

# Variables to manage state
chase_active = False
pulsate_active = False

def main():
    global chase_active, pulsate_active
    while True:
        inputValue = not inputPin.value
        inputValue1 = not inputPin1.value

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

        color_value = color_pot.value
        color_position = int((color_value / 65535.0) * 255)
        color = color_wheel(color_position)

        if chase_active:
            pot_value = speed_pot.value
            speed = 0 + (pot_value / 65535.0) * 40
            ChaseLights(speed, color)
        elif pulsate_active:
            pulsateLEDs(color)

        time.sleep(0.01)

if __name__ == "__main__":
    main()
