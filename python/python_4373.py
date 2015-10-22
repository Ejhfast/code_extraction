# Making shlex.split respect UNC paths
&gt;&gt;&gt; shlex.split(raw_args, posix=False)
['-path', '"\\\\server\\folder\\file.txt"', '-arg', 'SomeValue']
