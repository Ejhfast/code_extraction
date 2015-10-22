# Python - Sorting a dictionary {String Key: List of Strings} by len(value)?
&gt;&gt;&gt; d = {"A":["u","w"],"B":["t"],"C":["x","y","z"]}
&gt;&gt;&gt; sorted(d.items(), key=lambda x: len(x[1]), reverse=True)
[('C', ['x', 'y', 'z']), ('A', ['u', 'w']), ('B', ['t'])]
