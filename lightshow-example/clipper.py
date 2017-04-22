from lightshow import player
import time

file = 'goats'

player.play(file)
begin = time.time()

start = raw_input("Start? ")
start_time = time.time()
stop = raw_input("Stop? ")
stop_time = time.time()

print "player.clip('" + file + "'," + str(start_time - begin) + "," + str(stop_time-start_time) + ")"

