# Simple python command to capture shell execution output?
&gt;&gt;&gt; import subprocess
&gt;&gt;&gt; tagname = subprocess.check_output('git describe --tags'.split())
