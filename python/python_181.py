# In Python, how I do use subprocess instead of os.system?
import subprocess
p=subprocess.Popen(args, stdout=subprocess.PIPE)
print p.communicate()[0]
