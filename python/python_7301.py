# Trying to turn inner and out tuples into inner and outer lists
&gt;&gt;&gt; data = (('A', 'B', 'C'), ('D', 'E', 'F'), ('H', 'I', 'J'))
&gt;&gt;&gt; [list(tup) for tup in data]
[['A', 'B', 'C'], ['D', 'E', 'F'], ['H', 'I', 'J']]
