# Split by \b when your regex engine doesn't support it
&gt;&gt;&gt; re.compile(r'(\W+)').split('hello, foo')
['hello', ', ', 'foo']
