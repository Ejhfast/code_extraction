# A simple way to remove multiple spaces in a string in Python
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.sub(' +',' ','The     quick brown    fox')
'The quick brown fox'
