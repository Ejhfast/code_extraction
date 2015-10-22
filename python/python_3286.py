# python tuple to dict
&gt;&gt;&gt; t = ((1, 'a'),(2, 'b'))
&gt;&gt;&gt; dict((y, x) for x, y in t)
{'a': 1, 'b': 2}
