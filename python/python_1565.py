# Extract string from between quotations
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.findall('"([^"]*)"', 'SetVariables "a" "b" "c" ')
['a', 'b', 'c']
