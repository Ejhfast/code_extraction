# How to sort the outer and inner sublist of a nested list in Python?
&gt;&gt;&gt; data =  [[1, .45, 0], [2, .49, 2], [3, .98, 0], [4, .82, 1], [5, .77, 1], [6, .98, 2] ]
&gt;&gt;&gt; sorted(data, key=lambda x:(x[2], -x[1]))
[[3, 0.98, 0], [1, 0.45, 0], [4, 0.82, 1], [5, 0.77, 1], [6, 0.98, 2], [2, 0.49, 2]]
