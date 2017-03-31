from gpiozero import MCP3008
from time import sleep


adc = MCP3008(channel=0)

def norm(v, minv, maxv):
   return int(v * maxv) + minv

def get():
   return adc.value

if __name__ == "__main__":
   while True:
      print str(adc.value) + "\t" + str(norm(adc.value, 0, 10))
      sleep(0.5)

