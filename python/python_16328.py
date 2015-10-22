# Python: Can I add every other integer in a list?
&gt;&gt;&gt; L = [2,4,8,9,4,2]
&gt;&gt;&gt; [sum(i) for i in itertools.zip_longest(*[iter(L)]*2, fillvalue=0)]
[6, 17, 6]
