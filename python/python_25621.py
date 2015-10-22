# Send input to command line prompt from Python program
from subprocess import Popen, PIPE
proc = Popen(['starcluster', 'terminate', 'cluster'], stdin=PIPE)
proc.stdin.write("y\r")
