# How do I send input to and get output from bc using Python?
p = subprocess.Popen("bc", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate('1+1\n')
