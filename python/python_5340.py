# Executing a command and storing its output in a variable
p = subprocess.Popen(["./pmm"], shell=False, stdout=subprocess.PIPE)
output = p.stdout.read()
