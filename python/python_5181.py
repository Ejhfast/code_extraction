# pythonic way to filter a dictionary of arrays
&gt;&gt;&gt; ks = set(random.sample(d, 2))
&gt;&gt;&gt; dict((k, list(ks &amp; set(d[k]))) for k in ks)
{'a': ['a', 'c'], 'c': ['a', 'c']}
