# Check memory usage of subprocess in Python
subprocess.Popen('ulimit -v 1024; ls', shell=True)
