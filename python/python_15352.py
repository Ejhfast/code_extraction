# Python: Split a string, respect and preserve quotes
&gt;&gt;&gt; s = r'a=foo, b=bar, c="foo, bar", d=false, e="false", f="foo\", bar"'
&gt;&gt;&gt; re.findall(r'(?:[^\s,"]|"(?:\\.|[^"])*")+', s)
['a=foo', 'b=bar', 'c="foo, bar"', 'd=false', 'e="false"', 'f="foo\\", bar"']
