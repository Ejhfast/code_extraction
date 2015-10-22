# Python- can I split a string with str.split after the first integer?
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.split(r'(?&lt;=\d)\D', 'start 123 after text', maxsplit=1)
['start 123', 'after text']
