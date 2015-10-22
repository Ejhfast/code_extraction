# Pandas Very Simple Percent of total size from Group by
df.groupby('col1').size().apply(lambda x: float(x) / df.groupby('col1').size().sum()*100)
