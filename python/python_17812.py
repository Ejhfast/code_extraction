# finding and returning names and counts of duplicate values in Python list
&gt;&gt;&gt; ns=[2, 2, 2, 0, 2, 1, 3, 3]
&gt;&gt;&gt; {x: ns.count(x) for x in set(ns) if ns.count(x) &gt; 1}
{2: 4, 3: 2}
