# 7zip Commands from Python
import subprocess
cmd = ['7z', 'a', 'Test.7z', 'Test', '-mx9']
sp = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
