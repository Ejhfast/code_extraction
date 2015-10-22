# How to run processes in the background and override standard streams
import subprocess
p = subprocess.Popen(["mycmd", "--somearg"], stdout=subprocess.PIPE)
out, err = p.communicate()
