# In Python - how to execute system command with no output
import os
import subprocess
subprocess.call(["ls", "-l"], stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
