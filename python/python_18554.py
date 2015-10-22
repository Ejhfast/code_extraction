# Passing control of console window to subprocess
from subprocess import Popen
Popen('gdb a.out', shell=True).communicate()
print 'test'
