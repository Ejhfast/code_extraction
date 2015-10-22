# arbitrary sequences in "zipped" sequences (mapped sequences actually)
&gt;&gt;&gt; from itertools import izip_longest
&gt;&gt;&gt; [list(x) for x in itertools.izip_longest([1,2,3],[4,5,6,7],['a','b'])]
[[1, 4, 'a'], [2, 5, 'b'], [3, 6, None], [None, 7, None]]
