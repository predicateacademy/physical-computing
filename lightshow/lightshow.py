from gpiozero import PWMLED
import time
import lightshow_patterns as lsp


led = [ PWMLED(4), PWMLED(17), PWMLED(27), PWMLED(22), PWMLED(5), PWMLED(6),
        PWMLED(13),PWMLED(19), PWMLED(26), PWMLED(18), PWMLED(23), PWMLED(24),
        PWMLED(25),PWMLED(12), PWMLED(16), PWMLED(20)]

def run(pattern, delay) :
   for p in pattern:
      for i in range(len(p)):
         led[i].value = float(p[i])
      time.sleep(delay)

def pulse(on_time=1.0, off_time=1.0):
   for x in led:
      x.pulse(on_time, off_time, None, True)

def blink(on_time=1.0, off_time=1.0):
   for x in led:
      x.blink(on_time, off_time, None, True)

def off(delay=0.0):
   run(lsp.off(led), delay)

def on(delay=0.0):
   run(lsp.on(led), delay)

def on_odd(delay=0.0):
   run(lsp.on_odd(led), delay)

def on_even(delay=0.0):
   run(lsp.on_even(led), delay)   

def splitout(delay=0.25):
   run(lsp.splitout(), delay)

def splitin(delay=0.25):
   run(lsp.splitin(), delay)

def throw_right(delay=0.02):
   run(lsp.throw_right(led), delay)

def throw_left(delay=0.02):
   run(lsp.throw_left(led), delay)

def fill_right(delay=0.2):
   run(lsp.fill_right(led), delay)

def fill_left(delay=0.2):
   run(lsp.fill_left(led), delay)

def clear_right(delay=0.2):
   run(lsp.clear_right(led), delay)

def clear_left(delay=0.2):
   run(lsp.clear_left(led), delay)

def left_right(delay=0.2):
   run(lsp.left_right(led), delay)

def right_left(delay=0.2):
   run(lsp.right_left(led), delay)

