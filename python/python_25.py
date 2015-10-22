# Split a string by spaces -- preserving quoted substrings -- in Python
&gt;&gt;&gt; import shlex
&gt;&gt;&gt; shlex.split('this is "a test"')
['this', 'is', 'a test']
