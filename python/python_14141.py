# Python : Splitting multidimensional lists
&gt;&gt;&gt; L = [(('a', 'c'), -3), (('a', 'd'), -7), (('c', 'd'), -4)]
&gt;&gt;&gt; zip(*[(a[0], a[1], b) for a, b in L])
[('a', 'a', 'c'), ('c', 'd', 'd'), (-3, -7, -4)]
