# How to store the return value of os.system that it has printed to stdout in python?
import subprocess
p = subprocess.Popen('my_command', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, error = p.communicate()
