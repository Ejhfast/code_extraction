# Outputting with Willie bot doesn't work, but print does
process = subprocess.Popen(command,shell=True, stderr=subprocess.PIPE)
output = process.stderr.read()
