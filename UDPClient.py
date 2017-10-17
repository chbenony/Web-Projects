#UDPClient.py
#from time import time
import time
#from time import *
#from socket import socket, SOCK_DGRAM, AF_INET
from socket import *

serverName = 'localhost'
serverPort = 1998

clientSocket = socket(AF_INET, SOCK_DGRAM)
#1 second timeout
clientSocket.settimeout(1)

try:
        message = raw_input('Input lowercase sentence: ')
        send_time_ms = time.time()
        clientSocket.sendto(message, (serverName, serverPort))
        modifiedMessage, addr = clientSocket.recvfrom(4096)
        print modifiedMessage, addr

except timeout:
        print "timeout"
        recv_time_ms = time.time()
        rtt_in_ms = round(recv_time_ms - send_time_ms, 3)
        print "Round Trip Time (RTT): %d"% rtt_in_ms

"""clientSocket.settimeout(1)
message = raw_input('Input lowercase sentence: ')
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, addr = clientSocket.recvfrom(4098)

try:
        modifiedMessage, addr = clientSocket.recvfrom(4096)
except timeout:
        print "timeout"
#print modifiedMessage, addr
clientSocket.close()
"""
clientSocket.close()
                                       