from gpiozero import MCP3008
from time import sleep
from lightshow import *

pot1 = MCP3008(channel=0)
pot2 = MCP3008(channel=1)
v1 = pot1.value
v2 = pot2.value

while True:
   n1v = round(pot1.value, 1)
   n2v = round(pot2.value, 1)
   if n1v != v1 or n2v != v2:
      v1 = n1v
      v2 = n2v
      pulse(v1, v2)
   sleep(1)
