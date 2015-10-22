# Partial Variable length string removal in Python
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.sub('(s|S)uite\s+\w+\s*', '', 'Suite 134A xxx')
'xxx'
