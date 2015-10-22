# Get all combinations of list elements not ignoring position in Python
&gt;&gt;&gt; from itertools import product
&gt;&gt;&gt; list(product([1, 2], repeat=2))
[(1, 1), (1, 2), (2, 1), (2, 2)]
