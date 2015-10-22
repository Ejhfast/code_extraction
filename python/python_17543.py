# Un-nesting nested lists
&gt;&gt;&gt; L = [[[1,2,3]], [[4,5,6]], [[7,8,9]]]
&gt;&gt;&gt; [x[0] for x in L]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
