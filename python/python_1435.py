# Python scientific notation using D instead of E
&gt;&gt;&gt; val = "1.5698D+03"  # 1,569.8
&gt;&gt;&gt; print float(val.replace('D', 'E'))
1569.8
