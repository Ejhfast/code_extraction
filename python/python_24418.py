# How to make a set of lists
&gt;&gt;&gt; l = [[1, 2, 3], [2, 4, 5], [1, 2, 3], [2, 4, 5]]
&gt;&gt;&gt; set(tuple(i) for i in l)
{(1, 2, 3), (2, 4, 5)}
