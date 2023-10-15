import time
from rpi_ws281x import *
import argparse
import math

# LED strip configuration:
LED_COUNT      = 300     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 25      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


def lightAllPixelsColor(strip, color):
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
            

def changeBrightness(strip, originalBrightness, newBrightness, seconds):
    currentBrightness = originalBrightness
    increasing = (originalBrightness < newBrightness)
    loops = abs(newBrightness-originalBrightness)
    time_waiting = seconds / loops
    
    for i in range(loops):
        if increasing:
            currentBrightness += 1
        else:
            currentBrightness -= 1
            
        strip.setBrightness(currentBrightness)
        strip.show()
        time.sleep(time_waiting)

def colorWipe(strip, color, total_time=50):
    """Wipe color across display a pixel at a time."""
    used_time = 0
    i = 0
    while (used_time < total_time):
        timeA = time.time_ns()
        strip.setPixelColor(i, color)
        strip.setPixelColor(strip.numPixels()-i, color)
        strip.show()
        used_time += (time.time_ns() - timeA) / 1000000
        i += 1

    
# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        i = 0
        while i < 70:
            i += 1
            strip.setBrightness(i)
            lightAllPixelsColor(strip, Color(255, 0, 0))
            time.sleep(0.1)
            lightAllPixelsColor(strip, Color(0, 0, 0))
            time.sleep(.225)
            lightAllPixelsColor(strip, Color(255, 0, 0))
            time.sleep(0.1)
            lightAllPixelsColor(strip, Color(0, 0, 0))
            time.sleep(.575)
        
        brightness = strip.getBrightness()
        while True:
            lightAllPixelsColor(strip, Color(127, 127, 127))
            changeBrightness(strip, brightness, 1, 3.75)
            strip.setBrightness(brightness)
            lightAllPixelsColor(strip, Color(255, 0, 0))
            changeBrightness(strip, brightness, 1, 3.75)
            strip.setBrightness(brightness)
            time.sleep(0.50)
            colorWipe(strip, Color(127,127,127), 500)
            changeBrightness(strip, brightness, 1, 2.75)
            strip.setBrightness(brightness)
            lightAllPixelsColor(strip, Color(255, 140, 0))
            changeBrightness(strip, brightness, 1, 3.75)
            strip.setBrightness(brightness)
            lightAllPixelsColor(strip, Color(255, 255, 0))
            changeBrightness(strip, brightness, 1, 3.75)
            strip.setBrightness(brightness)
            lightAllPixelsColor(strip, Color(0, 255, 0))
            changeBrightness(strip, brightness, 1, 3.75)
            strip.setBrightness(brightness)
            time.sleep(0.50)
            colorWipe(strip, Color(127,127,127), 500)
            changeBrightness(strip, brightness, 1, 2.75)
            strip.setBrightness(brightness)
            lightAllPixelsColor(strip, Color(0, 0, 255))
            changeBrightness(strip, brightness, 10, 2.50)
            strip.setBrightness(brightness)
            strip.show()
            time.sleep(0.25)
            lightAllPixelsColor(strip, Color(127, 127, 127))
            time.sleep(.175)
            lightAllPixelsColor(strip, Color(0, 0, 255))
            time.sleep(0.175)
            lightAllPixelsColor(strip, Color(127, 127, 127))
            time.sleep(0.5)
            lightAllPixelsColor(strip, Color(138, 43, 226))
            changeBrightness(strip, brightness, 1, 3.75)
            strip.setBrightness(brightness)    
    except KeyboardInterrupt:
        if args.clear:
            lightAllPixelsColor(strip, Color(0,0,0))
    