# Python, split list of coordinates, based on x
&gt;&gt;&gt; l = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1)]
&gt;&gt;&gt; left = [ x for x in l if x[0] &lt; 2]
&gt;&gt;&gt; right = [ x for x in l if x[0] &gt;= 2]
