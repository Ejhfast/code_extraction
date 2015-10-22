# How to get process's grandparent id
os.popen("ps -p %d -oppid=" % os.getppid()).read().strip()
