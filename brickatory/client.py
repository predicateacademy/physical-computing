#!/usr/bin/env python
 
import sys
sys.path.append('gen-py')
 
from brickatory import BrickatoryService
from brickatory.ttypes import *
from brickatory.constants import *
 
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transport = None
client = None

def init():
  global transport
  global client

  # Make socket
  transport = TSocket.TSocket('predicate.us', 30303)
 
  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)
 
  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
 
  # Create a client to use the protocol encoder
  client = BrickatoryService.Client(protocol)
 
  # Connect!
  transport.open()

def join(name, brick_width, brick_height, paddle_width, paddle_height, ball_radius):
  try:
    init()
    ret = client.join(name, brick_width, brick_height, paddle_width, paddle_height, ball_radius)
    if ret == -2:
      print 'Hacker Alert! PLAYER ' + name + ' DISQUALIFIED. No changes to game code permitted.'
      sys.exit(0)

    if ret == -1:
      print 'Cheater! Cheater! Pumpkin Eater! ' + name + ' already played a game.'
      sys.exit(0)

  
  except Thrift.TException, tx:
    print "join %s" % (tx.message)
    sys.exit

def report(name, state):
  try:
    nm = PlayerState()
    nm.name = name
    nm.state = state
    client.report(nm)
    if state == 3:
      print 'PLAYER ' + name + ' Lost.'
      sys.exit(0)
    if state == 2:
      print 'YOU WON!!'
      sys.exit(0)   
  except Thrift.TException, tx:
    print "report %s" % (tx.message)
    sys.exit

def status():
  try:
    lst = client.status()
    for x in lst:
      if x.state == 2:
        print 'GAME OVER: Player ' + x.name + ' won.'
        return False
    return True
  except Thrift.TException, tx:
    print "status %s" % (tx.message)
    sys.exit

