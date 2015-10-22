# Pandas: Get unique MultiIndex level values by label
In [11]: df.index.get_level_values('co').unique()
Out[11]: array(['DE', 'FR'], dtype=object)
