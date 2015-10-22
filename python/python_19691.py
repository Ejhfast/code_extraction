# Using regex to find multiple matches on the same line
&gt;&gt;&gt; r = re.compile(r"\&lt;\'.*?\'\&gt;")
&gt;&gt;&gt; r.findall(s)
["&lt;'found'&gt;", "&lt;'one'&gt;", "&lt;'three'&gt;", "&lt;'matches'&gt;", "&lt;'found'&gt;"]
