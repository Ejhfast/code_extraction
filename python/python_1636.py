# Can Python's list comprehensions (ideally) do the equivalent of 'count(*)...group by...' in SQL?
&gt;&gt;&gt; values = [1,1,1,2]
&gt;&gt;&gt; print [(x,values.count(x)) for x in set(values)]
[(1, 3), (2, 1)]
