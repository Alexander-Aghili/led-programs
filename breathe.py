#!/bin/python3

#External imports
import time
from rpi_ws281x import *
import math

#Interal imports
from strip_config import *
from music import *
from arg_parser import *
from clear import *
from general import *
            

def changeBrightness(strip, music, originalBrightness, newBrightness, beats):
    currentBrightness = originalBrightness
    increasing = (originalBrightness < newBrightness)
    loops = abs(newBrightness-originalBrightness)
    time_waiting = beats / loops
    
    for i in range(loops):
        if increasing:
            currentBrightness += 1
        else:
            currentBrightness -= 1
            
        strip.setBrightness(currentBrightness)
        strip.show()
        music.waitBeats(time_waiting)
    
# Main program logic follows:
if __name__ == '__main__':
    args = argParser()
    
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    
    speaktome_tempo = 120
    music = Music(speaktome_tempo)

    try:
        #Speak to me
        for i in range(1, 71):
            strip.setBrightness(i)
            lightAllPixelsColor(strip, Color(255, 0, 0))
            music.waitBeats(1/4)
            lightAllPixelsColor(strip, Color(0, 0, 0))
            music.waitBeats(1/2)
            lightAllPixelsColor(strip, Color(255, 0, 0))
            music.waitBeats(1/4)
            lightAllPixelsColor(strip, Color(0, 0, 0))
            music.waitBeats(1)
        
        #Breathe (in the air)
        music.waitBeats(1/4)
        music.setTempo(128) #Breathe tempo
        brightness = strip.getBrightness()
        while True:
            lightAllPixelsColor(strip, Color(127, 127, 127))
            changeBrightness(strip, music, brightness, 1, 8)
            strip.setBrightness(brightness)
            lightAllPixelsColor(strip, Color(255, 0, 0))
            changeBrightness(strip, music, brightness, 1, 8)
            strip.setBrightness(brightness)
            music.waitBeats(3/4)
            colorWipeRunners(strip, Color(127,127,127), 500)
            changeBrightness(strip, music, brightness, 1, 6)
            strip.setBrightness(brightness)
            lightAllPixelsColor(strip, Color(255, 140, 0))
            changeBrightness(strip, music, brightness, 1, 8)
            strip.setBrightness(brightness)
            lightAllPixelsColor(strip, Color(255, 255, 0))
            changeBrightness(strip, music, brightness, 1, 8)
            strip.setBrightness(brightness)
            lightAllPixelsColor(strip, Color(0, 255, 0))
            changeBrightness(strip, music, brightness, 1, 8)
            strip.setBrightness(brightness)
            music.waitBeats(3/4)
            colorWipeRunners(strip, Color(127,127,127), 500)
            changeBrightness(strip, music, brightness, 1, 6)
            strip.setBrightness(brightness)
            lightAllPixelsColor(strip, Color(0, 0, 255))
            changeBrightness(strip, music, brightness, 10, 6)
            strip.setBrightness(brightness)
            strip.show()
            lightAllPixelsColor(strip, Color(127, 127, 127))
            music.waitBeats(1/2)
            lightAllPixelsColor(strip, Color(0, 0, 255))
            music.waitBeats(1/2)
            lightAllPixelsColor(strip, Color(127, 127, 127))
            music.waitBeats(1)
            lightAllPixelsColor(strip, Color(138, 43, 226))
            changeBrightness(strip, music, brightness, 1, 8)
            strip.setBrightness(brightness)    
    except KeyboardInterrupt:
        if args.clear:
            instantClear(strip)
    