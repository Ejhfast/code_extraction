# Pandas: Sum up rows by group
weightsDf.sum(axis=1).groupby(level=[0,1]).sum()
