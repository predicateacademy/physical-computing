from time import *
from lightshow import player

# play at 24.5 sec for 2.2 sec
player.clip("goats", 24.5, 2.2)

# start at 24.5 sec
player.clip("goats", 24.5)

# add a sleep here to keep our code alive
sleep(15)
