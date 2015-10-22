# How to get stdout into a string (Python)
from subprocess import *
output = Popen(["mycmd", "myarg"], stdout=PIPE).communicate()[0]
