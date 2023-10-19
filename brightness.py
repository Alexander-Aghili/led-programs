#!/bin/python3
#External imports
import time
from rpi_ws281x import *

#Internal imports
from strip_config import *
from arg_parser import *
from clear import *
from general import *
    
def slowlyChangeBrightness(strip, maxBrightness, wait, increase):
    brightness = 0
    for i in range(maxBrightness):
        time.sleep(wait/1000)
        if increase:
            brightness = i
        else:
            brightness = maxBrightness - i
            
        strip.setBrightness(brightness)
        strip.show()
            
# Main program logic follows:
if __name__ == '__main__':
    args = argParser()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    try:
        strip.setBrightness(0)
        lightAllPixelsColor(strip, Color(127, 127, 127))
        slowlyChangeBrightness(strip, 100, 100, True)
        slowlyChangeBrightness(strip, 100, 100, False)
        strip.show()
    except KeyboardInterrupt:
        if args.clear:
            instantClear(strip)