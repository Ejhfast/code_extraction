# How to let the output being printed on the interactive shell with subprocess
p = subprocess.Popen('pwd', stdout = subprocess.PIPE)
p.communicate() # returns (stdout, None)
