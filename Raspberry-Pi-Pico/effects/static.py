def staticLEDs(strip, color):
    print("Static LEDs")
    for i in range(strip.n):
        strip[i] = color
    
    strip.write()