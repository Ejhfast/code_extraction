# how to select column values to display in pandas groupby
In [92]: df.groupby(['A']).apply(lambda x: x['B'].tolist()).to_dict()
Out[92]: {10: [100, 101], 20: [102]}
