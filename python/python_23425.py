# Calling sar in Python is producing weird results
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, bufsize=0)
    for line in p.stdout:
        count += 1
