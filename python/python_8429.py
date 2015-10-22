# List comprehension and or spacing with a new-line
&gt;&gt;&gt; test = {'a' : None, 'b' : None}
&gt;&gt;&gt; b = (','.join([k for k in test if test[k]])
...      or 'hello')
