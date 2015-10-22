# is there a way to join list of strings in sublist
&gt;&gt;&gt; L = [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g']]
&gt;&gt;&gt; [[''.join(x)] for x in L]
[['ab'], ['cd'], ['ef'], ['g']]
