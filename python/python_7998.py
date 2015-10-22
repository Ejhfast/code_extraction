# How to run a python script from another python script and get the returned status code?
import subprocess
retcode = subprocess.call(["/usr/bin/python", "/path/to/test.py"])
print "Return code of test.py is ", retcode
