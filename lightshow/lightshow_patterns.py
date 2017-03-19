import time

def flip(pattern):
   p = ''
   for i in range(len(pattern)):
      if pattern[i] == '0':
         p += '1'
      else:
         p += '0'
   return p

def flips(patterns):
   ret = []
   for pattern in patterns:
      ret.append(flip(pattern))
   return ret

def off(led):
	patterns = []
	pattern = ''
	for x in range(len(led)):
		pattern += '0'
	patterns.append(pattern)
	return patterns

def on(led):
	patterns = []
	pattern = ''
	for x in range(len(led)):
		pattern += '1'
	patterns.append(pattern)
	return patterns

def on_odd(led):
   pattern = ''
   for x in range(len(led)):
      if x % 2 == 0:
        pattern += '0'
      else:
        pattern += '1'
   return [pattern]

def on_even(led):
   return flips(on_odd(led))

def splitout():
	patterns = []
	patterns.append('0000000110000000')
	patterns.append('0000001001000000')
	patterns.append('0000010000100000')
	patterns.append('0000100000010000')
	patterns.append('0001000000001000')
	patterns.append('0010000000000100')		
	patterns.append('0100000000000010')		
	patterns.append('1000000000000001')		
	return patterns

def splitin():
	patterns = []
	patterns.append('1000000000000001')
	patterns.append('0100000000000010')
	patterns.append('0010000000000100')
	patterns.append('0001000000001000')
	patterns.append('0000100000010000')
	patterns.append('0000010000100000')
	patterns.append('0000001001000000')		
	patterns.append('0000000110000000')		
	return patterns


def throw_right(led):
   patterns = []
   for x in range(len(led)):
      l = left_right(led)
      for item in l:
         for idx in range(x):
            tlist = list(item)
            tlist[len(tlist)-idx-1] = '1'
            item = ''.join(tlist)
         patterns.append(item)
   patterns.extend(on(led))
   return patterns

def throw_left(led):
   patterns = []
   for x in range(len(led)):
      l = right_left(led)
      for item in l:
         for idx in range(x):
            tlist = list(item)
            tlist[idx] = '1'
            item = ''.join(tlist)
         patterns.append(item)
   patterns.extend(on(led))
   return patterns

def fill_right(led):
   patterns = []
   for x in range(len(led)):
      l = off(led)
      for item in l:
         for idx in range(x):
            tlist = list(item)
            tlist[len(tlist)-idx-1] = '1'
            item = ''.join(tlist)
         patterns.append(item)
   patterns.extend(on(led))
   return patterns

def fill_left(led):
   patterns = []
   for x in range(len(led)):
      l = off(led)
      for item in l:
         for idx in range(x):
            tlist = list(item)
            tlist[idx] = '1'
            item = ''.join(tlist)
         patterns.append(item)
   patterns.extend(on(led))
   return patterns

def clear_right(led):
   patterns = []
   for x in range(len(led)):
      l = on(led)
      for item in l:
         for idx in range(x):
            tlist = list(item)
            tlist[len(tlist)-idx-1] = '0'
            item = ''.join(tlist)
         patterns.append(item)
   patterns.extend(off(led))
   return patterns

def clear_left(led):
   patterns = []
   for x in range(len(led)):
      l = on(led)
      for item in l:
         for idx in range(x):
            tlist = list(item)
            tlist[idx] = '0'
            item = ''.join(tlist)
         patterns.append(item)
   patterns.extend(off(led))
   return patterns

def left_right(led):
   patterns = []
   for x in range(len(led)):
      pattern = ''
      for y in range(len(led)):
         if x == y:
            pattern += '1'
         else:
            pattern += '0'
      patterns.append(pattern)
   return patterns

def right_left(led):
   rt = left_right(led)
   rt.reverse()
   return rt



