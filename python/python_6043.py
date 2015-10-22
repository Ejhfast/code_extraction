# Python - Find non mutual items in two dicts
&gt;&gt;&gt; dict(set(a.iteritems()) ^ set(b.iteritems()))
{'a': 1, 'e': 5, 'd': 4}
