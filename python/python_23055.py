# Python Pandas multi-index values not moving over in pivot table
&gt;&gt;&gt; idx = pd.MultiIndex.from_tuples(cols)
&gt;&gt;&gt; p_table = p_table.reindex_axis(idx.get_level_values(1), axis=1)
&gt;&gt;&gt; p_table.columns = idx
