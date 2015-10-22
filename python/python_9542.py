# Python: getting lowest integer in list of tuples
&gt;&gt;&gt; nums = [(), (), ('24', '25', '26', '27'), (), (), (), ()]
&gt;&gt;&gt; min(int(j) for i in nums for j in i)
24
