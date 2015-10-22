# `elif` in list comprehension conditionals
&gt;&gt;&gt; l = [1, 2, 3, 4, 5]
&gt;&gt;&gt; ['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in l]
['yes', 'no', 'idle', 'idle', 'idle']
