# Trying to call a shell command with Python, gets nothing
p = subprocess.Popen(command, shell=True, bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
