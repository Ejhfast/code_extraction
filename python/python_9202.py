# Convert numpy array to tuple
&gt;&gt;&gt; arr = numpy.array(((2,2),(2,-2)))
&gt;&gt;&gt; tuple(map(tuple, arr))
((2, 2), (2, -2))
