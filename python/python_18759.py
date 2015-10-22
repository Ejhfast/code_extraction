# Python nested list slicing
&gt;&gt;&gt; [[n[0] for n in l]] + [u[1:] for u in l]
[['A', 'B', 'C', 'D'], ['A1', 1, 2, 3], ['A2', 4, 5, 6], ['A3', 7, 8, 9], ['A4', 10, 11, 12]]
