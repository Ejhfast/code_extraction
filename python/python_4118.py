# Find indices of elements equal to zero from numpy array
&gt;&gt;&gt; x = numpy.array([1,0,2,0,3,0,4,5,6,7,8])
&gt;&gt;&gt; numpy.where(x == 0)[0]
array([1, 3, 5])
