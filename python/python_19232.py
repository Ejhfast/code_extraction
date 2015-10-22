# Pandas groupby: storing only indexes
&gt;&gt;&gt; groups = df.groupby(['code','colour']).groups
&gt;&gt;&gt; groups['one','white']
[1L, 6L]
