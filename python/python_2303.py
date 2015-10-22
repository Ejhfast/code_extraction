# How do I retrieve program output in Python?
import subprocess
proc = subprocess.Popen(['java', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc.communicate()
