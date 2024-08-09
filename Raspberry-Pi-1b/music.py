import time
import pygame
import RPi.GPIO as GPIO
import adafruit_character_lcd.character_lcd as characterlcd
import board
import digitalio
import serial
from eventLoop import eventLoop, pauzeLoop
import sys
from lib.TimedEvent import TimedEvent

# Configuration
# Filename, loop, bpm
# All files should be at a sample rate of 48000 kHz
MP3_FILE_1 = ("/home/bert/FunFun-2024/Raspberry-Pi-1b/music/levendbewijsopzet1.ogg", eventLoop, 160)
MP3_FILE_2 = ("/home/bert/FunFun-2024/Raspberry-Pi-1b/music/europapa.ogg", pauzeLoop, 160)

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
pygame.mixer.init(frequency=48000)

print("Pygame mixer initialized")

# UART configuration
ser = serial.Serial('/dev/serial0', 9600)
print("UART initialized")

lcd.clear()  # Clear the LCD screen
previous_lcd_message = ("", "")
active_song = MP3_FILE_1

def knop_volgende_event():
    global active_song, startTime
    print("Trigger Bewoondef")
    
    if active_song == MP3_FILE_2:
        return
    
    pygame.mixer.music.stop()
    pygame.mixer.music.load(MP3_FILE_2[0])
    pygame.mixer.music.play()
    
    active_song = MP3_FILE_2
    
    resetAllEffects(MP3_FILE_2[1])
    
    writeLCD_line_2("GO > Pauze")
    startTime = millis()
    
def knop_mode_event():
    print("Mode knop")
    
def knop_vorige_event():
    global active_song, startTime
    print("Vorige nummer")
    
    if active_song == MP3_FILE_1:
        return
    
    pygame.mixer.music.stop()
    pygame.mixer.music.load(MP3_FILE_1[0])
    pygame.mixer.music.play()
    
    active_song = MP3_FILE_1
    
    resetAllEffects(MP3_FILE_1[1])
    
    writeLCD_line_2("GO > Main")
    startTime = millis()  
    
def knop_play_pauze_event():
    print("Play/Pauze")

buttonEvents = [{
    "pin": Knop_volgende,
    "callback": knop_volgende_event
}, {
    "pin": Knop_mode,
    "callback": knop_vorige_event
}, {
    "pin": Knop_vorige,
    "callback": knop_mode_event
}, {
    "pin": Knop_play_pauze,
    "callback": knop_play_pauze_event
}]

def sendCommand(event: TimedEvent, currentRelativeTime):
    # Format the command and send it to the Pico
    command = f"{event.formatCommand()}-{active_song[2]}"
    
    # If stop, make console color red else green
    print(f"\033[92m{currentRelativeTime} | Command sent: {command} on group: {event.group.value}\033[0m")
    
    ser.write((command + "\n").encode())
    
    return True

def writeLCD(line_1: str, line_2: str):
    global previous_lcd_message
    message = line_1 + "\n" + line_2
    
    if message == previous_lcd_message:
        return
    
    lcd.clear()
    lcd.message = message
    
    previous_lcd_message = (line_1, line_2)
    
def writeLCD_line_1(line_1: str):
    if previous_lcd_message[0] == line_1:
        return
    
    writeLCD(line_1, previous_lcd_message[1])
    
def writeLCD_line_2(line_2: str):
    if previous_lcd_message[1] == line_2:
        return
    
    writeLCD(previous_lcd_message[0], line_2)

def millis():
    return time.time() * 1000

# This makes sure all effects are reset and can be started again
def resetAllEffects(loop):
    for event in loop:
        event.hasStarted = False
        event.hasStopped = False

startTime = millis()

def main():
    global active_song, startTime
    
    # Log all registered events
    print("-------------------")
    print("Registered events:")
    
    print("Registered for Main:")
    for event in MP3_FILE_1[1]:
        print(event.formatCommand())
        
    print("Registered for Pauze:")
    for event in MP3_FILE_2[1]:
        print(event.formatCommand())
    
    print("-------------------")
    
    # print the current time
    print(f"Current time: {startTime}")
    
    print("Starting main loop...")
    
    last_time = 500000 # Make sure the first loop runs
    last_button_press = 5000 # Make sure the first button press is not too fast
    
    # Main loop
    while True:
        # Check for button presses
        for buttonEvent in buttonEvents:
            if not GPIO.input(buttonEvent["pin"]):
                # Make sure the button press is not too fast
                if millis() - last_button_press > 500:
                    last_button_press = millis()
                    buttonEvent["callback"]()
           
        # Restart the current song if it has ended
        # also ensure it is loaded
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(active_song[0])
            pygame.mixer.music.play()
            startTime = millis()
            resetAllEffects(active_song[1])
           
        # Check every 500ms
        if millis() - last_time >= 100:
            last_time = millis()
            currentTime = millis()
            
            currentRelativeTime = int(currentTime - startTime)
            
            writeLCD_line_1(f"{int((currentTime - startTime) / 1000)}s {active_song[0].replace('/home/bert/FunFun-2024/Raspberry-Pi-1b/music/', '')}")
                
            for event in active_song[1]:
                if event.hasStopped:
                    continue
                
                groupNumber = event.group.value.replace("LEDKAST_", "")

                if event.shouldStart(currentTime, startTime):
                    sendCommand(event, currentRelativeTime)
                    writeLCD_line_2(f"{groupNumber} > START {event.effect.value}")
        time.sleep(0.001)
                    
main()
