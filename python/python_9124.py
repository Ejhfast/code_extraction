# Delete (a,b) from a python list of tuples if (b,a) exists
&gt;&gt;&gt; import itertools
&gt;&gt;&gt; list(itertools.combinations((1, 2, 3), 2))
[(1, 2), (1, 3), (2, 3)]
