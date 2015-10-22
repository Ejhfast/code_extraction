# Get all indexes for a python list
&gt;&gt;&gt; l = [1,2,3,1,1]
&gt;&gt;&gt; [index for index, value in enumerate(l) if value == 1]
[0, 3, 4]
