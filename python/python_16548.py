# Handling Shell Redirection in Python subprocess.Popen()
cmd = './test.sh &gt; /tmp/ttt.log'
p = subprocess.Popen(cmd, shell = True)
