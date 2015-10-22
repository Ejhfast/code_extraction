# Calling a python script that returns a value from perl
p = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE, shell=True)
print p.communicate()[0]
