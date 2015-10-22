# Splitting a string with multiple delimiters in Python
import re
re.split(r'[,;]+', 'This,is;a,;string')
&gt; ['This', 'is', 'a', 'string']
