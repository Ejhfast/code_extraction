# How to use map function on nested lists and converting strings to integers?
&gt;&gt;&gt; line=[['10', '13\n'], ['3', '4\n'], ['5', '3\n'], ['1', '13']]
&gt;&gt;&gt; map(lambda X:([int(X[0])+1, int(X[1]) +1]),line)
[[11, 14], [4, 5], [6, 4], [2, 14]]
