# Python get N elements from a list at a time using lambda
&gt;&gt;&gt; import itertools
&gt;&gt;&gt; itertools.izip(a, itertools.islice(a,1,None))
