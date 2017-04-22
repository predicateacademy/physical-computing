import lightshow as show
import fsr
import time

def to_pattern(val):
    patterns = []
    pattern = list('0000000000000000')

    for x in range(val):
        pattern[x] = '1'
        patterns.append(''.join(pattern))

    return patterns

while True:
    val = fsr.norm(fsr.get(), 0, 16)
    
    if val > 0:
        pattern = to_pattern(val)
        show.run(pattern, 0.1)
        time.sleep(3)
        show.off()
                
    time.sleep(0.25)
