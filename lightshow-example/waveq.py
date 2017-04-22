#!/usr/bin/env python

# 8 band Audio equaliser from wav file
# Original code from Space Gerbil
# http://www.raspberrypi.org/phpBB3/viewtopic.php?p=314087
 
import alsaaudio as aa
from struct import unpack
import numpy as np
import wave
import threading
import sys
import time
import copy
import subprocess, os
import math

# Initialise matrix
matrix    = np.array([0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0])
power     = []
weighting = [1,1,1,1, 10,10,10,10, 10,10,10,10, 1,1,1,1]
# Set up audio
wavfile = None
sample_rate = None
no_channels = None
chunk       = 4096 

def play(path, callback):
    global wavfile, sample_rate, no_channels, matrix
    wavfile = wave.open(path,"r")
    sample_rate = wavfile.getframerate()
    no_channels = wavfile.getnchannels()

    output = aa.PCM(aa.PCM_PLAYBACK, aa.PCM_NORMAL)
    output.setchannels(no_channels)
    output.setrate(sample_rate)
    output.setformat(aa.PCM_FORMAT_S16_LE)
    output.setperiodsize(chunk)

    data = wavfile.readframes(chunk)
    while data!='':
        output.write(data)   
        matrix=calculate_levels(data, chunk,sample_rate,matrix)
        pattern = ''.join(str(e) for e in matrix.tolist())
        print pattern
        if callback != None:
            callback([pattern])
        data = wavfile.readframes(chunk)

# Return power array index corresponding to a particular frequency
def piff(val):
    return int(2*chunk*val/sample_rate)
   
def calculate_levels(data, chunk,sample_rate,matrix):
#    global matrix
    # Convert raw data (ASCII string) to numpy array
    data = unpack("%dh"%(len(data)/2),data)
    data = np.array(data, dtype='h')
    # Apply FFT - real data
    fourier=np.fft.rfft(data)
    # Remove last element in array to make it the same size as chunk
    fourier=np.delete(fourier,len(fourier)-1)
    # Find average 'amplitude' for specific frequency ranges in Hz
    power = np.abs(fourier) 

    matrix[0]= int(np.mean(power[piff(0)    :piff(1250):1]))
    matrix[1]= int(np.mean(power[piff(1250)  :piff(2500):1]))
    matrix[2]= int(np.mean(power[piff(2500)  :piff(3750):1]))
    matrix[3]= int(np.mean(power[piff(3750)  :piff(5000):1]))
    matrix[4]= int(np.mean(power[piff(5000) :piff(6250):1]))
    matrix[5]= int(np.mean(power[piff(6250) :piff(7500):1]))
    matrix[6]= int(np.mean(power[piff(7500) :piff(8750):1]))
    matrix[7]= int(np.mean(power[piff(8750):piff(10000):1]))
    matrix[8]= int(np.mean(power[piff(10000):piff(11250):1]))
    matrix[9]= int(np.mean(power[piff(11250):piff(12500):1]))
    matrix[10]= int(np.mean(power[piff(12500):piff(13750):1]))
    matrix[11]= int(np.mean(power[piff(13750):piff(15000):1]))
    matrix[12]= int(np.mean(power[piff(15000):piff(16250):1]))                    
    matrix[13]= int(np.mean(power[piff(16250):piff(17500):1]))    
    matrix[14]= int(np.mean(power[piff(17500):piff(18750):1]))
    matrix[15]= int(np.mean(power[piff(18750):piff(20000):1]))    
    #print matrix.tolist()
    # Tidy up column values for the LED matrix
    matrix=np.divide(np.multiply(matrix,weighting),25000)
    
    #print matrix.tolist()
    matrix=matrix.clip(0,1) 
    return matrix


if __name__ == "__main__":
    try:
        # Process audio file   
        print "Processing....."
        play("music/fireworks.wav", None)

    except KeyboardInterrupt:
        print "User Cancelled (Ctrl C)"

    except:
        print "Unexpected error - ", sys.exc_info()[0], sys.exc_info()[1]
        raise
