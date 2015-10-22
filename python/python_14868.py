# in python How to add to the windows path variable to find executables
import subprocess
proc = subprocess.Popen('hello.exe',shell=True)
proc.wait()
