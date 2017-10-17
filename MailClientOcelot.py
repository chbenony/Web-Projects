#!/usr/bin/python

import socket
import time
"""
/* 
 * Following code has been provided by Professor Downey
 ** / """

def send_recv(socket, msg, code):
	if msg != None:
		print "Sending==> ", msg
		socket.send(msg + '\r\n')

		recv = socket.recv(1024)
		if recv[:3] != code:
			print '%s reply not received from server' % code
		return recv

def send(socket, msg):
	print "Sending==> ", msg
	socket.send(msg + '\r\n')

serverName = 'smtp.cis.fiu.edu'
serverPort = 25

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
recv = (clientSocket, None, '220')

clientName = 'tim'
userName = "downeyt"
userServer = "cs.fiu.edu"
toName= "timdotdowney"
toServer="gmail.com"

#Send HELO command and print server response
heloCommand = 'HELO %s' % clientName

#Send MAIL FROM command and print server response.
fromCommand = 'MAIL FROM: <%s@%s>' % (userName, userServer)
recvFrom = send_recv(clientSocket, fromCommand, '250')

#Send RCPT TO command and print server response
rcptCommand = 'RCPT TO: <%s@%s>' % (toName, toServer)
recvRcpt = send_recv(clientSocket, rcptCommand, '250')

#Send DATA command and print server response.
dataCommand = 'DATA'
dataRcpt = send_recv(clientSocket, dataCommand, '354')

#Send message data.
send(clientSocket, "Date; %s" % time.strftime("%a, %d %b %Y %H:%S -0400", time.localtime()));
send(clientSocket, "From: Tim Downey <%s@%s>" % (userName, userServer));
send(clientSocket, "Subject: Simple Mail Message");
send(clientSocket, "To: %s@%s" % (toName, toServer));
send(clientSocket, ""); #End of headers

send(clientSocket, "Hello World");
send(clientSocket, "Bonjour le Monde!");
send(clientSocket, "ocelot client");

#Message ends with a single period.
send_recv(clientSocket, ".", '250');

#Send QUIT command and get server response.
quitCommand = 'QUIT'
quitRcpt = send_recv(clientSocket, quitCommand, '221')
