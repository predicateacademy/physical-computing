from time import *
from lightshow import *

print 'lights on'
on()
sleep(3)

print 'lights off'
off()
sleep(3)

print 'odd lights on'
on_odd()
sleep(3)

print 'even lights on'
on_even()
sleep(3)

print 'split out from center (default 0.25 delay)'
splitout()
sleep(3)

print 'split in from center (0.5 delay)'
splitin(0.25)
sleep(3)

print 'throwing to the right (default delay)'
throw_right()
sleep(3)

print 'throwing to the left (0.01 delay)'
throw_left(0.01)
sleep(3)

print 'filling lights from the right (default delay)'
fill_right()
sleep(3)

print 'filling lights from the left (0.1 delay)'
fill_left(0.1)
sleep(3)

print 'clear lights from the right (default delay)'
clear_right()
sleep(3)

print 'clear lights from the left (0.1 delay)'
clear_left(0.1)
sleep(3)

print 'move left to right'
left_right()
sleep(3)

print 'move right to left'
right_left()
sleep(3)

patterns = []
patterns.append('0000000110000000')
patterns.append('0000001111000000')
patterns.append('0000011111100000')
patterns.append('0000111111110000')
patterns.append('0001111111111000')
patterns.append('0011111111111100')    
patterns.append('0111111111111110')    
patterns.append('1111111111111111')
patterns.append('0111111111111110')
patterns.append('0011111111111100') 
patterns.append('0001111111111000')
patterns.append('0000111111110000')
patterns.append('0000011111100000')
patterns.append('0000001111000000')
patterns.append('0000000110000000')    
run(patterns, 0.1)
