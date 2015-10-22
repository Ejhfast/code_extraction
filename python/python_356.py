# Python - Acquire value from dictionary depending on location/index in list
&gt;&gt;&gt; indices = [index for index, i in enumerate(m) if i == 4]
&gt;&gt;&gt; h = [d[i][0] for i in indices]
