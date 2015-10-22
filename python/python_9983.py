# Select an array from a multidimensional array
&gt;&gt;&gt; a = [['id123','ddf',1],['id456','ddf',1],['id789','ddf',1]]
&gt;&gt;&gt; next(x for x in a if x[0] == 'id456')
['id456', 'ddf', 1]
