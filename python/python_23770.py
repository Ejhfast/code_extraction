# Run Putty command from python
import subprocess
proc_args = ['metl', '-m', 'arg2', ....]
process = subprocess.Popen(proc_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
