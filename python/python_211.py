# python: list comprehension tactics
&gt;&gt;&gt; st = 'asdf'
&gt;&gt;&gt; [st[:n+1] for n in range(len(st))]
['a', 'as', 'asd', 'asdf']
