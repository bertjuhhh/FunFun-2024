import time
import pygame
import RPi.GPIO as GPIO
import adafruit_character_lcd.character_lcd as characterlcd
import board
import digitalio
import serial
from eventLoop import eventLoop
from lib.TimedEvent import TimedEvent


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
previous_lcd_message = ("", "")
active_song = MP3_FILE_1

def knop_volgende_event():
    print("Trigger Bewoondef")
    pygame.mixer.music.stop()
    pygame.mixer.music.load(MP3_FILE_2)
    pygame.mixer.music.play()
    
    active_song = MP3_FILE_2
    
    writeLCD_line_2("Gestart> Bewoonddef")
    
def knop_mode_event():
    print("Mode knop")
    
def knop_vorige_event():  
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

def sendCommand(event: TimedEvent, startOrStop: str):
    # Format the command and send it to the Pico
    # Format example: "START DMX1 TWINKLE rgb(255, 0, 0)"
    command = event.formatCommand()
    command = f"{startOrStop} {command}"
    
    ser.write(command.encode())
    print(f"Command sent: {command} on group: {event.group}")
    
    return True

def writeLCD(line_1: str, line_2: str):       
    message = line_1 + "\n" + line_2
    
    if (message == previous_lcd_message):
        return
    
    lcd.clear()
    lcd.message = message
    
    previous_lcd_message = message
    
def writeLCD_line_1(line_1: str):
    writeLCD(line_1, previous_lcd_message[1])
    
def writeLCD_line_2(line_2: str):
    writeLCD(previous_lcd_message[0], line_2)

def main():
    startTime = time.time()
    # Convert starttime to ms
    startTime = startTime * 1000
    
    # Main loop
    while True:
        # Loop the music
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(active_song)
            pygame.mixer.music.play()
            startTime = time.time() * 1000
            
        currentTime = time.time() * 1000
        
        # On the first line of the LCD, display the current song, together with how long it has been playing
        writeLCD_line_1(f"{MP3_FILE_1} {int(currentTime - startTime)}s")
        
        # Check for button presses
        for button in buttonEvents:
            if GPIO.input(button["pin"]) == 0:
                button["callback"]()
                time.sleep(0.2)
        
        # Check for timed events
        for event in eventLoop:
            # Event has already stopped, so we can skip it
            if (event.hasStopped == True):
                continue
            
            # The event has not started and should start
            if (event.shouldStart(currentTime, startTime) and not event.hasStarted):
                sendCommand(event, "START")
                writeLCD_line_2(f"{event.group}> START {event.effect}")
                
            # The event has started and should stop
            if (event.shouldStop(currentTime, startTime) and not event.hasStopped):
                sendCommand(event, "STOP")
                writeLCD_line_2(f"{event.group}> STOP {event.effect}")
                
            # Sleep for 10ms
            time.sleep(0.01)
        
        
# Run the main function
main()