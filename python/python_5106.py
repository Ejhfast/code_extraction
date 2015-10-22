# pythonic way of finding a value in a list which hasn't been supplied
&gt;&gt;&gt; supplied_list = [0, 1]
&gt;&gt;&gt; list(set(range(3)) - set(supplied_list))
[2]
