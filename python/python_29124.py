# "No such file or directory" error when calling fc-list in python
import subprocess
 cmd = '/usr/local/bin/fc-list'
 output = subprocess.Popen(cmd, stdout=subprocess.PIPE ).communicate()[0]
