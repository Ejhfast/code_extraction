# Is there a function in Python to split a string without ignoring the spaces?
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.split(r"(\s+)", "This is the string I want to split")
['This', ' ', 'is', ' ', 'the', ' ', 'string', ' ', 'I', ' ', 'want', ' ', 'to', ' ', 'split']
