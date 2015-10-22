# Iterate the start of a list without any import in Python
&gt;&gt;&gt; xs = [1, 2, 3, 4, 5, 6, 7]
&gt;&gt;&gt; [x for i in range(3) for x in xs[i::3]]
[1, 4, 7, 2, 5, 3, 6]
