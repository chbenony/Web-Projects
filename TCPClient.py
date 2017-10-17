
from socket import socket, AF_INET, SOCK_STREAM
serverName = 'localhost'
serverPort = 1998
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = raw_input('Input lowercase sentence: ')
clientSocket.send(message)
modifiedMessage = clientSocket.recv(4096)
print 'From Server: ', modifiedMessage
clientSocket.close()
~                                                                                                  
~                                                                                                  
~                                                                                                  
~               