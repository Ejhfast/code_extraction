# Generating families of lambda functions
&gt;&gt;&gt; fns = [(lambda x,y = y: x == y) for y in range(10)]
&gt;&gt;&gt; map(lambda x: x(1), fns)
[False, True, False, False, False, False, False, False, False, False]
