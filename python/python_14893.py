# How do you remove the nth index of a nested list?
&gt;&gt;&gt; x = [(1, 2, 3), (1, 2, 3), (1, 2, 3)]
&gt;&gt;&gt; x = [(a, b) for (a, b, c) in x]
[(1, 2), (1, 2), (1, 2)]
