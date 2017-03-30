from lightshow import *
from time import *

while True:
   h = int(strftime("%I", localtime()))
   m = int(strftime("%M", localtime()))
   s = int(strftime("%S", localtime()));
   print str(h) + ":" + str(m) + ":" + str(s)
   pattern = '{0:04b}'.format(h) + '{0:06b}'.format(m) + '{0:06b}'.format(s)
   run([pattern], 0.5) 
