# Python list inter-element operation - can this be done with list comprehension?
&gt;&gt;&gt; x = [1.,2.,3.,4.]
&gt;&gt;&gt; [ ((e-f)/f) for e,f in zip ( x[:-1], x[1:]) ]
[-0.5, -0.3333333333333333, -0.25]
