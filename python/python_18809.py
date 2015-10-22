# Getting a string from subprocess.call?
p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE)
somestr = p.stdout.readline()
