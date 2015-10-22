# What is the most elegant way of finding the n-length consecutive sub-lists of a list in Python?
&gt;&gt;&gt; some_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
&gt;&gt;&gt; l = [some_lst[i:i+3] for i in xrange(len(some_lst)-2)]
