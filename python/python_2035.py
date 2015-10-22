# How do I translate Ruby's IO.popen calls into Python's subprocess.Popen calls?
&gt;&gt;&gt; import subprocess
&gt;&gt;&gt; io = subprocess.Popen('ls', stdout=subprocess.PIPE).stdout
&gt;&gt;&gt; for line in io: print(line.strip())
