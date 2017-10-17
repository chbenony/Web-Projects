
#!/usr/bin/python3

#collections.py
#example taken from Professor Tim Downey's public scripts web page

import os
import sys

sys.stderr = sys.stdout
print ("Content-type: text/plain\n")

colors = ['red', 'green', 'blue']
print ("A list prints in a string format: {0}".format(colors))
print ("Print the second element in the list: {0}".format(colors[1]))
colors[1] = 'yellow'
print ("Change the second element in the list to {0[1]}: {0}".format(colors))

teams = ('marlins', 'dolphins', 'heat')
print ("A tuple prints in a string format: {0}",format(teams))
print ("Print the second element in the list: {0[1]}".format(teams))
print ("Change the second element in the list: {0[1]}".format(teams))
try:
   team[1] = 'panthers'
   print ("Change the second element in the list to {0[1]}: {0}",format(teams))
except:
	print ("Error: cannot modify a tuple")

person = {'age': 23, 'major': 'CS', 'gpa': 3.7}
print ("A dictionary prints in a string format: {0}".format(person))
print ("Print the major from the dictionary: {0[major]".format(person))
person['major'] = 'IT'
print ("Change the major in the dictionary to {0[major]}: {0}".format(person))

