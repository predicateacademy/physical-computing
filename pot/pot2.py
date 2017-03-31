from gpiozero import MCP3008
from time import sleep

pot1 = MCP3008(channel=0)
pot2 = MCP3008(channel=1)

while True:
   print str(pot1.value) + "," + str(pot2.value)
   sleep(0.5)
