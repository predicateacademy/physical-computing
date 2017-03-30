from time import *
from lightshow import *
i = 0

while True:
   if i % 65536 == 0:
      i = 0
   run(['{0:016b}'.format(i)], 0.1)
   i = i + 1


