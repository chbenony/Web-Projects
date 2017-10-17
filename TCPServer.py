from socket import socket, SOCK_STREAM, AF_INET

#Create a TCP socket
#Notice the use of SOCK_StREAM for TCP packets
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 1998

#Assign IP address and port number to socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print ("Interrupt with CTRL-C")

while True:
        try:
                #Establish the connection
                print ("Ready to serve...")
                connectionSocket, addr = serverSocket.accept()
                message = connectionSocket.recv(2048).decode()
                print (message)
                filename = message.split()[1].partition("/")[2]
                #print filename
                open(filename)
                print ("The file %s exists! " % filename)
                connectionSocket.send(message.encode())
                connectionSocket.close()

        except IOError:
                print ("Not found %s" % filename)
                #connectionSocket.send("HTTP/1.1 404 File Not Found".endcode())
                connectionSocket.send("HTTP/1.1 404 File Not Found".encode())
                connectionSocket.close()
        except KeyboardInterrupt:
                print ("\nInterrupted by CTRL-C")
                break
serverSocket.close()