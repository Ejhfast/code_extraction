# Accessing matlab terminal from python
subprocess.call(["matlab", "-nosplash", "-nodesktop", "-r", "command1;command2;"], shell=True, stdin=subprocess.PIPE, stout=subprocess.PIPE)
