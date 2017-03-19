import pygame, random
from mutagen.mp3 import MP3
from time import sleep
from os import listdir

pygame.init()
pygame.mixer.init()
path = 'music/'
current_file = None

def load(file):
	global current_file
	file = path + file
	if file.endswith(".mp3") == False:
		file += ".mp3"
	current_file = MP3(file)
	pygame.mixer.music.load(file)

def rand(file, play_time):
	load(file)
	length = current_file.info.length
	start_time = length - play_time - (random.random() * length)
	pygame.mixer.music.play(start=start_time)
	sleep(play_time)
	pygame.mixer.music.stop()

def clip(file, start_time, play_time):
	load(file)
	print 'clipping file ' + file
	pygame.mixer.music.play(start=start_time)
	sleep(play_time)
	pygame.mixer.music.stop()

def play(file):
	load(file)
	if pygame.mixer.music.get_busy() == False:
        	pygame.mixer.music.play()
	#while pygame.mixer.music.get_busy():
	#	sleep(1)

def stop():
        pygame.mixer.music.stop()

def pick():
	return random.choice(listdir(path))

if __name__ == "__main__":
	#for x in range(10):
		#clip("wall", 8, 2.5)
		#clip("goats", 24.5, 2.2)
	while True:
		clip(pick(), 0, 15)
