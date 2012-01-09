#!/usr/bin/python

'''Initial imports'''
try:
  import SocketServer
except ImportError:
  print 'Please install SocketServer module : sudo easy_install SocketServer'

try:
  from xbee import XBee
except ImportError:
  print 'Please install XBee module : sudo easy_install XBee'

try:
  import serial
except ImportError:
  print 'Please install serial module : sudo easy_install pySerial'
import sys

if sys.argv[1]:
  '''Check whether we specified modem device '''
  serial_modem = sys.argv[1]
  print "Attaching to %s" % serial_modem
  try:
    '''XBee initialization to 'ser' handler and to 'xbee' object'''
    ser = serial.Serial(serial_modem, 9600)
    xbee = XBee(ser)
    pass
  except serial.serialutil.SerialException,error:
    '''If the serial modem is invalid we have to throw an exception '''
    print "Could not attach to serial modem => %s" % error
    raise
else:
  ''' If there's no serial modem given that raise exception '''
  print 'Please provide working serial modem e.g. /dev/ttyUSB0' 
  raise



class IphoneRequestHandler(SocketServer.BaseRequestHandler ):
    '''Iphone request handler class logic begins here '''
    def setup(self):
        '''Initial greeint sent to client after connection'''
        print self.client_address, 'connected!'
        self.request.send('Hi - this is cesar request handler v.0.1' + str(self.client_address) + '\n')
        self.request.send('---------------------- \n')
        self.request.send('Listening for commands \n')

    def handle(self):
        data = 'dummy'
        while data:
            '''start receiving data from client'''
            data = self.request.recv(1024)
            print "Received from client: %s" % data
            if data.strip() == 'A':
              '''If received 'A' letter from iphone, we send command to xbee'''
              print "Sending command to xbee.."
              xbee.send('lightOnRequest: true')
            elif data.strip() == 'B':
              '''If received 'B' letter from iphone, we send command to xbee'''
              print "Sending command to xbee.."
              xbee.send('lightOffRequest: true')
            elif data.strip() == 'exit':
              ''' On exit - detach from serial device '''
              ser.close()
              return
            else:
              print 'Unknown command'
              self.request.send("Server answer: unknown command" + '\n')

    def finish(self):
        ''' Some finish routines '''
        print self.client_address, 'disconnected!'
        self.request.send('bye ' + str(self.client_address) + '\n')

''' Initially turn off the bulb '''
xbee.send('lightOffRequest: true')
''' Instantiate server '''
server = SocketServer.ThreadingTCPServer(('', 31415), IphoneRequestHandler)
''' Start the server ''' 
server.serve_forever() 
''' When finished - detach from modem device '''
ser.close()
