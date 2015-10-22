# How do I convert characters like "&#58;" to ":" in python?
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.sub("&amp;#(\d+);",lambda x:unichr(int(x.group(1),10)),"&amp;#58; or &amp;#46;")
u': or .'
