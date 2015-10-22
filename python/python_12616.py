# Python: Optimized method of cutting/slicing sorted lists
&gt;&gt;&gt; import bisect
&gt;&gt;&gt; a[bisect.bisect_left(a, 6):]
[7, 9]
