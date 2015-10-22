# How to generate an alternating range?
&gt;&gt;&gt; [b for a in ((x,-x) for x in range(1, 10 + 1)) for b in a]
[1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]
