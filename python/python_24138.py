# Number of permutations of a set with an element limited to some positions
&gt;&gt;&gt; from itertools import permutations
&gt;&gt;&gt; len([x for x in permutations((1, 3, 5, 0, 9)) if x[0]!=0])
96
