# Calling main() of another python script and getting STDOUT result
proc = subprocess.Popen(['python', testRunner.tsPyFile, test], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdoutValue = proc.communicate()[0]
