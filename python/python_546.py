# Python, how to parse strings to look like sys.argv
&gt;&gt;&gt; import shlex
&gt;&gt;&gt; shlex.split('-o 1 --long "Some long string"')
['-o', '1', '--long', 'Some long string']
