#!/bin/python3

###########################################################
#
# Name: mbclient.py
# Author: Marco Tedaldi <mtedaldi@aequator.ch>
# Current Version: 0.1
# Revisions:
# 0.1   2020-02-13  Marco Tedaldi   Initial Version
#
#
# Description
# a simple Modbus Client that works from the command line
# as a client (master) to read and write tata over
# Modbus/TCP to a server (slave)
#
# Usage:
#
# Dependencies:
# Python3
# getopt
# pymodbus
#
###########################################################


import sys      # sys
import getopt   # read and parse command line options
import time     # we all need more of it!
from pymodbus.client.sync import ModbusTcpClient


def main(argv):
  ipaddress = ''
  port = 502
  action = ''
  target = ''
  data = ''
  try:
    opts, args = getopt.getopt(argv,"hi:p:a:t:d:",["help","ip=","port=","write","read", "target=", "data="])
  except getopt.GetoptError:
    print ('mbclient.py -h    #for help')
    print ('mbclient.py -i ipadress [-p port] -a {r|w} -t {coil,input,rega}')
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      print('help is on the way')
      time.sleep(1.8)
      print('maybe')
    elif opt in ("i", "ip"):
      ipaddress = arg
    elif opt in ("p", "port"):
      port = arg
    elif opt == "a":
      action = arg
    elif opt in ("write", "read"):
      action = opt
    elif opt in ("t", "target"):
      target = opt
    elif opt in ("d", "data"):
      data = opt
    else:
      print ("unknown optioni " + opt)

 



if __name__ == '__main__':
  main(sys.argv[1:])

'''
client = ModbusTcpClient('127.0.0.1')
client.write_coil(1, True)
result = client.read_coils(1,1)
print(result.bits[0])
client.close()
'''

