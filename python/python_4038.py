# Python - extracting a list of sub strings
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.findall("{{(.*?)}}", "this {{is}} a sample {{text}}")
['is', 'text']
