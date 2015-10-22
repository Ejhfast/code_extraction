# How can I capture the stdout output of a child process?
import subprocess
process = subprocess.Popen(["yourcommand"], stdout=subprocess.PIPE)
result = process.communicate()[0]
