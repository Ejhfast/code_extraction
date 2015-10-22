# In Python, what's the best way to get an unknown int from a string?
&gt;&gt;&gt;import re
&gt;&gt;&gt;re.findall(r'\d+', "My favorite chili was chili number 19")
['19']
