# Finding a tuple with greatest value
&gt;&gt;&gt; max(zip(first,second[0]),key=lambda x:max(x[1][1:]))[0]
('-2.50', '1.91', '2.03')
