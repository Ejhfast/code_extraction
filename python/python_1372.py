# Python 2.6: reading data from a Windows Console application. (os.system?)
import subprocess
foo = subprocess.Popen('test.exe',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
