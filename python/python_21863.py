# Get elements from dict using multiple keys
&gt;&gt;&gt; d = {'one':1, 'two':2, 'three':3, 'four':4}
&gt;&gt;&gt; [d[key] for key in 'one', 'three']
[1, 3]
