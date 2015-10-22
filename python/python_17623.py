# How to store os.system() output in a variable or a list in python
import subprocess
direct_output = subprocess.check_output('ls', shell=True) #could be anything here.
