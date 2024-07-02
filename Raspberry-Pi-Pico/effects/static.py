def staticLEDs(strip, ledCount, color):
    print ("Static LEDs")
    for i in range(ledCount):
        strip[i] = color
    
    strip.write()