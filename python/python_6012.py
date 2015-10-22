# Grouping Elements of Lists Within a List by Index
&gt;&gt;&gt; [list(t) for t in zip(*[[1,2,3], [4,5,6], [7,8,9]])]
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
