import time
import pygame
import RPi.GPIO as GPIO
import adafruit_character_lcd.character_lcd as characterlcd
import board
import digitalio

# Configuration
MP3_FILE_1 = "Pauzemuziek Getooid.mp3"
MP3_FILE_2 = "bewoonddef.mp3"
GPIO1_PIN = 7
GPIO2_PIN = 8
CONTROL_PIN_1 = 14
CONTROL_PIN_2 = 15
PROGRAM_PIN_1 = 9
PROGRAM_PIN_2 = 11

# LCD configuration
lcd_columns = 16
lcd_rows = 2

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
print("GPIO mode set to BCM")

# Raspberry Pi pin configuration for LCD:
lcd_rs = digitalio.DigitalInOut(board.D25)
lcd_en = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D23)
lcd_d5 = digitalio.DigitalInOut(board.D17)
lcd_d6 = digitalio.DigitalInOut(board.D18)
lcd_d7 = digitalio.DigitalInOut(board.D22)

# Initialize the LCD class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)
print("LCD initialized")

# Add a short delay to ensure proper initialization
time.sleep(0.5)

# Setup GPIO pins
GPIO.setup(GPIO1_PIN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(GPIO2_PIN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(CONTROL_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(CONTROL_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PROGRAM_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PROGRAM_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print("GPIO pins configured")

# Initialize pygame mixer
pygame.mixer.init()
print("Pygame mixer initialized")

# Timestamps for GPIO actions (in seconds)
GPIO1_ON_TIMES = [0, 60, 120]
GPIO1_OFF_TIMES = [20, 80, 140]
GPIO2_ON_TIMES = [30, 90, 150]
GPIO2_OFF_TIMES = [50, 110, 180]

def is_within_time_ranges(elapsed_time, on_times, off_times):
    for on, off in zip(on_times, off_times):
        if on <= elapsed_time < off:
            return True
    return False

def control_gpio(elapsed_time):
    # Initialize lcd_line_2 with a default value
    lcd_line_2 = "nu ffe niks"

    # Control GPIO1
    if is_within_time_ranges(elapsed_time, GPIO1_ON_TIMES, GPIO1_OFF_TIMES):
        GPIO.output(GPIO1_PIN, GPIO.LOW)  # Active low
        lcd_line_2 = "Programma 1"
    else:
        GPIO.output(GPIO1_PIN, GPIO.HIGH)

    # Control GPIO2
    if is_within_time_ranges(elapsed_time, GPIO2_ON_TIMES, GPIO2_OFF_TIMES):
        GPIO.output(GPIO2_PIN, GPIO.LOW)  # Active low
        lcd_line_2 = "Programma 2"
    else:
        GPIO.output(GPIO2_PIN, GPIO.HIGH)
    
    return lcd_line_2

try:
    current_mp3 = None
    previous_lcd_message = ("", "")
    lcd_line_2 = "nu ffe niks"
    lcd.clear()
    print("LCD cleared")
    
    while True:
        lcd_line_1 = "Stopped"
        
        if GPIO.input(CONTROL_PIN_1) == GPIO.LOW:  # Active low
            if current_mp3 != MP3_FILE_1:
                pygame.mixer.music.load(MP3_FILE_1)
                pygame.mixer.music.play(-1)  # Play on repeat
                current_mp3 = MP3_FILE_1
                start_time = time.time()
                print(f"Playing {MP3_FILE_1}")
        
        elif GPIO.input(CONTROL_PIN_2) == GPIO.LOW:  # Active low
            if current_mp3 != MP3_FILE_2:
                pygame.mixer.music.load(MP3_FILE_2)
                pygame.mixer.music.play(-1)  # Play on repeat
                current_mp3 = MP3_FILE_2
                start_time = time.time()
                print(f"Playing {MP3_FILE_2}")
        
        if GPIO.input(PROGRAM_PIN_1) == GPIO.LOW:  # Active low
            pygame.mixer.music.stop()
            current_mp3 = None
            GPIO.output(GPIO1_PIN, GPIO.LOW)  # Activate GPIO1
            GPIO.output(GPIO2_PIN, GPIO.HIGH) # Deactivate GPIO2
            lcd_line_1 = "Stopped"
            lcd_line_2 = "Programma 1"
            start_time = None
            print("Programma 1 activated")
        
        elif GPIO.input(PROGRAM_PIN_2) == GPIO.LOW:  # Active low
            pygame.mixer.music.stop()
            current_mp3 = None
            GPIO.output(GPIO2_PIN, GPIO.LOW)  # Activate GPIO2
            GPIO.output(GPIO1_PIN, GPIO.HIGH) # Deactivate GPIO1
            lcd_line_1 = "Stopped"
            lcd_line_2 = "Programma 2"
            start_time = None
            print("Programma 2 activated")

        if current_mp3:
            elapsed_time = time.time() - start_time
            lcd_line_1 = f"{current_mp3[:8]} {int(elapsed_time)}s"
            lcd_line_2 = control_gpio(elapsed_time)
            print(f"Elapsed time: {int(elapsed_time)} seconds", end="\r")
        else:
            print("Music stopped", end="\r")
        
        current_lcd_message = (lcd_line_1, lcd_line_2)
        
        if current_lcd_message != previous_lcd_message:
            lcd.clear()
            lcd.message = f"{lcd_line_1}\n{lcd_line_2}"
            previous_lcd_message = current_lcd_message
        
        # Sleep for a short period to prevent high CPU usage
        time.sleep(0.1)

finally:
    # Cleanup GPIO
    GPIO.cleanup()
    lcd.clear()
    print("GPIO cleaned up and LCD cleared")
