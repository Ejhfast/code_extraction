# Print to standard printer from Python?
import subprocess
lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
lpr.stdin.write(your_data_here)
