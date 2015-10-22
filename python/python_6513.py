# map(function, sequence) where function returns two values
&gt;&gt;&gt; a = [(0,1), (1,2), (2,3), (3,4), (4,5)]
&gt;&gt;&gt; zip(*a)
[(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]
