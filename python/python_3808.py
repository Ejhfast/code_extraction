# How can you convert a list of poorly formed data pairs into a dict?
&gt;&gt; s = "banana 4 apple 2 orange 4"
&gt;&gt; lst = s.split()
&gt;&gt; dict(zip(lst[::2], lst[1::2]))
