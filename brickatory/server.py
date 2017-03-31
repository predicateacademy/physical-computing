#!/usr/bin/env python
 
import sys
sys.path.append('gen-py')
 
from brickatory import BrickatoryService
from brickatory.ttypes import *
 
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
 
import socket
 
class BrickatoryServiceHandler:
  def __init__(self):
    self.log = {}
    self.active = {}
 
  def join(self, name, brick_width, brick_height, paddle_width, paddle_height, ball_radius):

    if name in self.active:
      print 'duplicate registration attempt from ' + name
      return -1

    if brick_width != 60 or brick_height != 15 or paddle_width != 60 or paddle_height != 12 or ball_radius != 8:
      print 'found a hacker ' + name
      return -2 

    print 'joining ' + name
    return 0

  def report(self, state):
     if state != None:
       self.active[state.name] = state

     return

  def status(self):
     return self.active.values()
 
handler = BrickatoryServiceHandler()
processor = BrickatoryService.Processor(handler)
transport = TSocket.TServerSocket(port=30303)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
 
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
 
print "Starting python server..."
server.serve()
print "done!"