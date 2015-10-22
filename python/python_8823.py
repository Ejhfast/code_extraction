# python calculating intervals using foldleft using lambda
&gt;&gt;&gt; l = [1, 2, 3, 4, 10]
&gt;&gt;&gt; [y-x for x, y in zip(l, l[1:])]
[1, 1, 1, 6]
