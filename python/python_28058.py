# How can I fill a DataFrame column with a list of e.g. 2 values in Pandas Python?
&gt;&gt;&gt; from itertools import cycle, islice
&gt;&gt;&gt; df['xyz'] = list(islice(cycle([0, 1]), len(df)))
