# Can I convert from a list of lists of arrays into a single list of arrays?
&gt;&gt;&gt; points = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
&gt;&gt;&gt; [x for p in points for x in p]
[[1, 2], [3, 4], [5, 6], [7, 8]]
