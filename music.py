#!/bin/python3

#External imports
import time

#Internal imports
from strip_config import * #Not necessary right but for later


ONE_MINUTE=60 #Seconds

class Music:
    tempo=100 #default 100
    
    def __init__(self, tempo: int):
        self.tempo = tempo

    def setTempo(self, tempo: int):
        self.tempo = tempo
        
    def getTempo(self):
        return self.tempo

    #Wait for certain number of beats
    def waitBeats(self, beats: float):
        x = self.tempo / beats
        wait_time = ONE_MINUTE/x
        time.sleep(wait_time)
        
