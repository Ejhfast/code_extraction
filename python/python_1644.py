# Python: Finding average of a nested list
&gt;&gt;&gt; import itertools
&gt;&gt;&gt; [sum(x)/len(x) for x in itertools.izip(*a)]
[4, 5, 6]
