# Get output of python script from within python script
proc = subprocess.Popen(['python', 'printbob.py',  'arg1 arg2 arg3 arg4'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print proc.communicate()[0]
