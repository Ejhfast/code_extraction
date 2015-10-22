# Generating a list of functions in python
&gt;&gt;&gt; basis = [ (lambda x,n=n: n*x) for n in [0, 1, 2] ]
&gt;&gt;&gt; print basis[0](1)
0
