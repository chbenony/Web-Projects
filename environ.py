#!/usr/bin/python3

import sys
import os

sys.stderr = sys.stdout

print ("Content-type: text/plain\n")

print ("Environment")

for param in os.environ.keys():
	print("%20s: %s" % (param, os.environ[param]))