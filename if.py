#!/usr/bin/python3

#if.py

import os
import sys

sys.stdout = sys.stderr

print ("Content-type: text/plain\n")

x = '99'
# originally was put as raw_input("Please enter a number: ")
# in python3, this would be changed to input("Please enter a number: ")

x_int = int(x)
#typecasted the string into an int
if (x_int > 100):
	print ('"' + x + '" is too large (original string x)')
	print ('"' + str(x_int) + '" is too large (x_int cast to str)')
	#Warning: removing this line will cause an error
	#remove the error by casting x back to a string with str(x)
	try:
		print ('"' + x_int + ' " is too large')
	except:
		print ("Error: Cannot combine string and int")
elif (x_int < 0): print (x_int, ' is too small')
else: print (x_int, ' is a valid grade')

print (0 <= x_int <= 100)