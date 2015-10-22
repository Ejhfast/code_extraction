# reading a file in python from different directory
import os
os.chdir('/foo/bar')
f = open('foobar.txt', 'r')
