# Match regex multiple times
&gt;&gt;&gt; import re
&gt;&gt;&gt; [m.start() for m in re.finditer(r'f(?=f)', 'fff')]
[0, 1]
