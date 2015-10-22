# creating a non-literal python tuple programmatically
&gt;&gt;&gt; m, n, k = 5, 7, 3
&gt;&gt;&gt; tuple(n if i == k else 1 for i in range(m))
(1, 1, 1, 7, 1)
