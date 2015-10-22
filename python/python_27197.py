# Regex not working normally in python
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.findall(r'(\?(.+?))\b', 'some text ?var etc')
[('?var', 'var')]
