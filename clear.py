#!/bin/python3
from rpi_ws281x import *

#Clear LEDs instantly
def instantClear(strip):
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()

#Clear LEDs slowly
def slowClear(strip):
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
        strip.show()
    
