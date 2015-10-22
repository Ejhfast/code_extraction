# Converting from list of tuples to list of lists of tuples
&gt;&gt;&gt; lst = [(1,2), (3,4), (5,6), (7,8), (9,10), (11,12), (13, 14), (15, 16), (17, 18)]
&gt;&gt;&gt; [lst[i:i+4] for i in xrange(0, len(lst), 4)]
[[(1, 2), (3, 4), (5, 6), (7, 8)], [(9, 10), (11, 12), (13, 14), (15, 16)], [(17, 18)]]
