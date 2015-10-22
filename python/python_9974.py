# Some tough string manipulation in Python
&gt;&gt;&gt; x = "foo(a) foo(something), foo(stuff)\n foo(1)"
&gt;&gt;&gt; re.sub(r'foo\(([^)]*)\)', r'\1', x)
u'a something, stuff\n 1'
