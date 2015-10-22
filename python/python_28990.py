# Get all connected device name on the network - Python
import subprocess
nmap = subprocess.Popen(('nmap'), stdout-subprocess.PIPE)
ipout = nmap.communicate()[0]
