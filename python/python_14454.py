# Python subprocess: how to retrieve the standard output
from subprocess import Popen, PIPE
p = Popen("./vecdiff.py file1 file2", stdout=PIPE, stderr=PIPE)
output, errput = p.communicate()
