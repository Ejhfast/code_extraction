# Spliting Variable to count groups of double characters
&gt;&gt;&gt; s="48657920697420776f726b73000000000000000000000000000000000000"
&gt;&gt;&gt; sum(1 if x == ('0','0') else 0 for x in zip(*[iter(s)]*2))
18
