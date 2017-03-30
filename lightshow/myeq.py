from lightshow import *
from time import *
import waveq

def callback(pattern):
	run(pattern, 0)

wav_file = 'music/fireworks.wav'
waveq.play(wav_file, callback)