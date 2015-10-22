# Python subprocess Popen stdout to variable only
import subprocess
p1 = Popen(["fping", '-C10', '-B1', '-p500','-r1', '-s', '172.29.172.106'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,error = p1.communicate()
