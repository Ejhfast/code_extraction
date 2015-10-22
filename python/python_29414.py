# Combinations of MultiIndex levels which occur in a DataFrame
In [22]: df.reset_index().set_index(['a','b']).index.unique()
Out[22]: array([(1, 'foo'), (2, 'foo'), (2, 'bar'), (3, 'foo'), (3, 'bar')], dtype=object)
