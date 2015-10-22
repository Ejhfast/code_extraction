# Splitting a string into words and punctuation
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.findall(r"[\w']+|[.,!?;]", "Hello, I'm a string!")
['Hello', ',', "I'm", 'a', 'string', '!']
