# subprocess.Popen not escaping command line arguments properly?
push = subprocess.Popen(s, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
