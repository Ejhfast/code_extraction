# Normalize DataFrame by group
In [10]: df.groupby('indx').transform(lambda x: (x - x.mean()) / x.std())
