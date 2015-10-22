# Comprehensions: multiple values per iteration
&gt;&gt;&gt; [sub for i in range(1, 4) for sub in (2*i, -2*i)]
[2, -2, 4, -4, 6, -6]
