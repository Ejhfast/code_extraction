# Python Pandas: Passing Multiple Functions to agg() with Arguments
df.groupby('A').agg([np.mean, lambda x: np.std(x, ddof=0)])
