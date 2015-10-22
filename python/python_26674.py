# Subprocess.Popen spits output on screen even with stdout=subprocess.PIPE)
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
