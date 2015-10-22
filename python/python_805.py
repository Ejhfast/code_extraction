# Disable console output from subprocess.Popen in Python
fh = open("NUL","w")
subprocess.Popen("taskkill /PID " + str(p.pid), stdout = fh, stderr = fh)
fh.close()
