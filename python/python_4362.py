# subprocess.check_output() doesn't seem to exist (Python 2.6.5)
&gt;&gt;&gt; import subprocess
&gt;&gt;&gt; output = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE).communicate()[0]
