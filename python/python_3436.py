# Getting the entire output from subprocess.Popen
p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True).communicate()[0]
