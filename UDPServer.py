#UDPServer.py

import random
from socket import socket, SOCK_DGRAM, AF_INET

#Create a UDP socket
#Notice the use of SOCK_DGRAM for UDP packets

serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('',1998))

#print "Waiting for connections"
print "Bound to 1998"
while True:
        #Generate random number in the range of 0 to 10
        rand = random.randint(0, 10)
        #Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(4096)
        #Capitalize the message from the client
        message = message.upper()
        #if rand is less than 4, we consider the packet lost and do not respond
        if rand < 4:
          continue
        #Otherwise, the server respond
        serverSocket.sendto(message, address)
"""
while True:
        #Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(4096)
        # Capitalize the message from the client
        print message, address
        message = message.upper()
        serverSocket.sendto(message, address)

while condition220:
        message = clientSocket.recv(4096)
        print message
        condition220 = message[0:6] != "220--"
message = send(clientSocket, "USER Anonymous")
message = send(clientSocket, "PASS downeyt@cs.fiu.edu")
message = send(clientSocket, "TYPE A")
message = send(clientSocket, "PASV")
start = message.find("(")
end = message.find(")")
tuple = message[start+1:end].split(',')
port = int(tuple[4])*256 + int(tuple[5])"""


serverSocket.close()
                       
                                                              19,1-8        66%

