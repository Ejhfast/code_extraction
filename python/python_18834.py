# Removing commutative pairs in a list in Python
&gt;&gt;&gt; {tuple(sorted(t)): t for t in list_1}.values()
[[0, 3], [3, 4]]
