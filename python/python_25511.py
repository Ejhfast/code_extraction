# Calling a command from external software using Popen() function
from subprocess import Popen, PIPE
proc = Popen(["ls", '-la'], stdout=PIPE) # if you want more, add after "-la"
print proc.stdout.readlines()
