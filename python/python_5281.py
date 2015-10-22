# Can't read stderr from subprocess.Popen
p = subprocess.Popen('ls', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
