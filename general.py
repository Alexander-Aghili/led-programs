#!/bin/python3
import time
from rpi_ws281x import *

# This function sets the color of all pixels in an LED strip to the specified color.
# It then updates the LED strip to display the new colors.
def lightAllPixelsColor(strip, color):
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    
#Display a color wipe effect on an LED strip.
# 
#This function sets all pixels in the strip to the specified color one pixel at a time
#with a specified delay between updates, creating a wipe effect.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
 
#Display a color wipe effect with multiple runners on an LED strip.
# 
#This function creates a color wipe effect where multiple "runners" move across
#the LED strip, each in a separate lane, with the specified color. The effect
#runs for a given total_time.
def colorWipeRunners(strip, color, total_time=50, num_runners=8):
    used_time = 0
    i = 0
    increment = strip.numPixels() / num_runners
    while (used_time < total_time):
        timeA = time.time_ns()
        for j in range(num_runners):
            try:
                strip.setPixelColor(i + int(j * increment), color)
            except:
                print("Overflow")
        strip.show()
        used_time += (time.time_ns() - timeA) / 1000000
        i += 1
        
def theaterChase(strip, color, wait_ms=50, iterations=50):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

"""Generate rainbow colors across 0-255 positions."""
def wheel(pos):
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

"""Draw rainbow that fades across all pixels at once."""
def rainbow(strip, wait_ms=20, iterations=1):
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

"""Draw rainbow that uniformly distributes itself across all pixels."""
def rainbowCycle(strip, wait_ms=20, iterations=5):
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

# Rainbow movie theater light style chaser animation.
def theaterChaseRainbow(strip, wait_ms=50):
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)
