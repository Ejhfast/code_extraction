# Scale a column of a list-of-lists in Python
&gt;&gt;&gt; [[j*((i==index)*(scale-1)+1) for i,j in enumerate(l)] for l in mtx]
[[0, 17, 2], [0, 17, 2], [0, 17, 2]]
