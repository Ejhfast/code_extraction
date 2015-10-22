# How do you add elements of a list together to make a string (python)
&gt;&gt;&gt; a = [[2,3], [4,5]]
&gt;&gt;&gt; ", ".join("{0} to {1}".format(n, p) for n, p in a)
'2 to 3, 4 to 5'
