# Break down this list using list comprehension
&gt;&gt;&gt; L = ['1,2,3', '22', '33']
&gt;&gt;&gt; [x for l in L for x in l.split(",")]
['1', '2', '3', '22', '33']
