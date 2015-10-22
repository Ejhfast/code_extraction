# Where clause with numpy
&gt;&gt;&gt; a = [[0.,0.,0.1,0.2], [0.,0.3,0.4,0.3], [0.,0.,0.1,0.]]
&gt;&gt;&gt; [i for i, xs in enumerate(a) if sum(xs) == 1]
[1]
