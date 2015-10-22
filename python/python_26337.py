# How to convert a dict of lists to a list of tuples of key and value in python?
&gt;&gt;&gt; y = {'a':[1,2,3], 'b':[4,5], 'c':[6]}
&gt;&gt;&gt; [(i,x) for i in y for x in y[i]]
[('a', 1), ('a', 2), ('a', 3), ('c', 6), ('b', 4), ('b', 5)]
