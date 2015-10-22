# How to efficiently remove the same-length elements from a list in python
&gt;&gt;&gt; l = [[1,3],[23,4],[13,45,6],[8,3],[44,33,12]]
&gt;&gt;&gt; dict((len(i), i) for i in l).values()
[[8, 3], [44, 33, 12]]
