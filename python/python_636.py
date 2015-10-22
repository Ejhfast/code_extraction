# Python and if statement
from subprocess import Popen, STDOUT
stdout, stderr = Popen('echo ' + cmd, shell=True, stderr=STDOUT).communicate()
print stdout
