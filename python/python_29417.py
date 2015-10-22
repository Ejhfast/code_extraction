# Changing a single index of a Series
idx = df.index.values
idx[3] = '2015-8-15'
df.index = idx
