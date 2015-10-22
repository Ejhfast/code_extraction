# Smallest way to expand a list by n
&gt;&gt;&gt; l = [1,2,3,4]
&gt;&gt;&gt; [it for it in l for _ in range(2)]
[1, 1, 2, 2, 3, 3, 4, 4]
