import time
import pygame
import RPi.GPIO as GPIO
import adafruit_character_lcd.character_lcd as characterlcd
import board
import digitalio
import serial
from eventLoop import eventLoop
from lib.TimedEvent import TimedEvent
import signal
import sys

# Configuration
MP3_FILE_1 = "Main.mp3"
MP3_FILE_2 = "Pauze.mp3"

Knop_volgende = 7
Knop_mode = 8
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

lcd.clear()  # Clear the LCD screen
previous_lcd_message = ("", "")
active_song = MP3_FILE_1

def knop_volgende_event():
    global active_song
    print("Trigger Bewoondef")
    pygame.mixer.music.stop()
    pygame.mixer.music.load(MP3_FILE_2)
    pygame.mixer.music.play()
    
    active_song = MP3_FILE_2
    
    writeLCD_line_2("Gestart> Bewoonddef")
    
def knop_mode_event():
    print("Mode knop")
    
def knop_vorige_event():
    global active_song
    print("Vorige nummer")
    pygame.mixer.music.stop()
    pygame.mixer.music.load(MP3_FILE_1)
    pygame.mixer.music.play()
    
    active_song = MP3_FILE_1  
    
    writeLCD_line_2("Gestart> Pauzemuziek")
    
def knop_play_pauze_event():
    print("Play/Pauze")
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

buttonEvents = [{
    "pin": Knop_volgende,
    "callback": knop_volgende_event
}, {
    "pin": Knop_mode,
    "callback": knop_mode_event
}, {
    "pin": Knop_vorige,
    "callback": knop_vorige_event
}, {
    "pin": Knop_play_pauze,
    "callback": knop_play_pauze_event
}]

def sendCommand(event: TimedEvent, startOrStop: str, currentRelativeTime):
    # Format the command and send it to the Pico
    command = event.formatCommand()
    command = f"{startOrStop} {command}"
    
    print(f"{currentRelativeTime}ms | Command sent: {command} on group: {event.group.value}")
    ser.write(command.encode())
    
    return True

def writeLCD(line_1: str, line_2: str):
    global previous_lcd_message
    message = line_1 + "\n" + line_2
    
    if message == previous_lcd_message:
        return
    
    lcd.clear()
    lcd.message = message
    
    previous_lcd_message = message
    
def writeLCD_line_1(line_1: str):
    if previous_lcd_message[1] == line_1:
        return
    
    writeLCD(line_1, previous_lcd_message[1])
    
def writeLCD_line_2(line_2: str):
    if previous_lcd_message[0] == line_2:
        return
    
    writeLCD(previous_lcd_message[0], line_2)

def millis():
    return int(time.time() * 1000)

# Flag to control the main loop
running = True

def signal_handler(sig, frame):
    global running
    print("Interrupt received, stopping...")
    running = False

def main():
    global active_song, running
    startTime = millis()
    
    # Register the SIGINT handler
    signal.signal(signal.SIGINT, signal_handler)
    
    # Log all registered events
    print("-------------------")
    print("Registered events:")
    
    for event in eventLoop:
        print(f"{event.start} >> {event.formatCommand()}")
    
    print("-------------------")
    
    # print the current time
    print(f"Current time: {startTime}")
    
    print("Starting main loop...")
    print("Hi from bert")
    
    pygame.init()
    
    # Main loop
    last_checked_time = millis()
    
    while running:
        currentTime = millis()
        
        # Only proceed if enough time has passed (e.g., 10 ms)
        if currentTime - last_checked_time >= 10:
            last_checked_time = currentTime
            
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(active_song)
                pygame.mixer.music.play()
                startTime = millis()
                
            currentRelativeTime = int(currentTime - startTime)
            
            writeLCD_line_1(f"{MP3_FILE_1} {int(currentRelativeTime / 1000)}s")
            
            for event in eventLoop:
                if event.hasStopped:
                    continue

                if event.shouldStart(currentTime, startTime):
                    sendCommand(event, "START", currentRelativeTime)
                    writeLCD_line_2(f"{event.group}> START {event.effect}")
                    
                if event.shouldStop(currentTime, startTime):
                    sendCommand(event, "STOP", currentRelativeTime)
                    writeLCD_line_2(f"{event.group}> STOP {event.effect}")
        
        # Process pygame events to keep the loop responsive
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()