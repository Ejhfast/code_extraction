# Merge rows of a dataframe in pandas based on a column
df = dataframe.groupby(['date', 'sitename', 'name']).sum()
