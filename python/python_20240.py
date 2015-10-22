# How to split a string containing digits and characters
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.findall("[a-z]+|[0-9]+", "abc123cde4567")
['abc', '123', 'cde', '4567']
