# Split sublist of a list into other sublists
&gt;&gt;&gt; x = [['a','b'],['c','f'],['q','w','t']]
&gt;&gt;&gt; [c for s in x for c in itertools.combinations(s, 2)]
[('a', 'b'), ('c', 'f'), ('q', 'w'), ('q', 't'), ('w', 't')]
