import lightshow as show
import fsr
import pot
import time

import pygame.mixer
from pygame.mixer import Sound
pygame.mixer.init()
drums = Sound("drums.wav")
lose = Sound("cry.wav")
win1 = Sound("win1.wav")
win2 = Sound("win2.wav")

def to_pattern(val):
    patterns = []
    pattern = list('0000000000000000')

    for x in range(val):
        pattern[x] = '1'
        patterns.append(''.join(pattern))

    return patterns

while True:
    val = fsr.norm(fsr.get(), 0, 16)
    pot_val = pot.norm(pot.get(), 0.01, 1)
    val = int(val / pot_val)
    if val > 16:
        val = 16
    print val
    drums.play(-1)
    
    if val > 0:
        drums.stop()
        pattern = to_pattern(val)
        show.run(pattern, 0.1)
        if val < 8:
            lose.play()
        elif val < 12:
            win1.play()
        else:
            win2.play()
            
        time.sleep(3)
        show.off()
                
    time.sleep(0.25)
