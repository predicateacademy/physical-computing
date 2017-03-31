from gpiozero import MCP3008
from time import sleep
from lightshow import *

adc = MCP3008(channel=0)
v = adc.value

while True:
   nv = round(adc.value, 1)
   if nv != v:
      v = nv
      pulse(v, v)
   sleep(1)
