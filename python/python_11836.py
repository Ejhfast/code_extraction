# How to obtain man page contents in Python?
p = subprocess.Popen(('man -P cat %s' % manTopic,), shell = True)
stdout, stderr = p.communicate()
if stdout:
