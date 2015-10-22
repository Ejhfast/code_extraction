# python: find only common key-value pairs of several dicts: dict intersection
&gt;&gt;&gt; dict(set.intersection(*(set(d.iteritems()) for d in dicts)))
{'a': 3}
