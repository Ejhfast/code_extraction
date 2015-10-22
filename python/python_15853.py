# How to take a python list index containing multiple strings and split it
&gt;&gt;&gt; l = [(1, 2, 3, 4, 5)]
&gt;&gt;&gt; [item for tup in l for item in tup]
[1, 2, 3, 4, 5]
