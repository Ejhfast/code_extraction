# Directing script output to a file using subprocess?
subprocess.Popen([sys.executable, "sub_script.py"], stdout=open("log.txt", "a"))
