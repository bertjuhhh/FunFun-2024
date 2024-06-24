import time
import pygame
import RPi.GPIO as GPIO
import adafruit_character_lcd.character_lcd as characterlcd
import board
import digitalio
import serial


# Configuration
MP3_FILE_1 = "Pauzemuziek Getooid.mp3"
MP3_FILE_2 = "bewoonddef.mp3"
Knop_volgende = 7 #14
Knop_mode = 8 #15
Knop_vorige = 9
Knop_play_pauze = 11

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
GPIO.setup(Knop_volgende, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Knop_mode, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Knop_vorige, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Knop_play_pauze, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print("GPIO pins configured")

# Initialize pygame mixer
pygame.mixer.init()
print("Pygame mixer initialized")

# UART configuration
ser = serial.Serial('/dev/serial0', 9600)
print("UART initialized")

lcd.clear() # beeldscherm leeg maken

# Timestamps for GPIO actions (in seconds)
Programma_1_aan = [0, 60, 120]
Programma_1_uit = [20, 80, 140]
Programma_2_aan = [30, 90, 150]
Programma_2_uit = [50, 110, 180]

def is_within_time_ranges(elapsed_time, on_times, off_times):
    for on, off in zip(on_times, off_times):
        if on <= elapsed_time < off:
            return True
    return False

def control_gpio(elapsed_time):
    # Initialize lcd_line_2 with a default value
    lcd_line_2 = "nu ffe niks"

    # Control Programma 1
    if is_within_time_ranges(elapsed_time, Programma_1_aan, Programma_1_uit):
        lcd_line_2 = "Programma 1"
        send_uart_command('c')
    else:
        send_uart_command('e')

    # Control Programma 2
    if is_within_time_ranges(elapsed_time, Programma_2_aan, Programma_2_uit):
        lcd_line_2 = "Programma 2"
        send_uart_command('p')
    else:
        send_uart_command('e')
    
    return lcd_line_2

def send_uart_command(command):
    ser.write(command.encode())

try:
    current_mp3 = None
    previous_lcd_message = ("", "")
    lcd_line_2 = "nu ffe niks"
    lcd.clear()
    send_uart_command('e') # alle leds uit
    print("LCD cleared")
    
    while True:
        lcd_line_1 = "Stopped"
        
        if GPIO.input(Knop_volgende) == GPIO.LOW:  # Active low
            if current_mp3 != MP3_FILE_1:
                pygame.mixer.music.load(MP3_FILE_1)
                pygame.mixer.music.play(-1)  # Play on repeat
                current_mp3 = MP3_FILE_1
                start_time = time.time()
                print(f"Playing {MP3_FILE_1}")
                send_uart_command('e')  # alle leds uit
        
        elif GPIO.input(Knop_mode) == GPIO.LOW:  # Active low
            if current_mp3 != MP3_FILE_2:
                pygame.mixer.music.load(MP3_FILE_2)
                pygame.mixer.music.play(-1)  # Play on repeat
                current_mp3 = MP3_FILE_2
                start_time = time.time()
                print(f"Playing {MP3_FILE_2}")
                send_uart_command('e')  # alle leds uit
        
        if GPIO.input(Knop_vorige) == GPIO.LOW:  # Active low
            pygame.mixer.music.stop()
            current_mp3 = None
            lcd_line_1 = "Stopped"
            lcd_line_2 = "Programma 1"
            send_uart_command('c')  
            start_time = None
            print("Programma 1 activated")
        
        elif GPIO.input(Knop_play_pauze) == GPIO.LOW:  # Active low
            pygame.mixer.music.stop()
            current_mp3 = None
            lcd_line_1 = "Stopped"
            lcd_line_2 = "Programma 2"
            send_uart_command('p')
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
    ser.close()
    print("GPIO cleaned up, LCD cleared, UART closed")
