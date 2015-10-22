# How to pass on regex argument to another script through SSH
import subprocess
output = subprocess.check_output(['ssh', 'otherserver', 'python', '/home/log/scripts/script2.py', regex])
