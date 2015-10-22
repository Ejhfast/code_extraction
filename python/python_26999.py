# sum of values larger than median of each row in pandas dataframes
quantile = 0.75  # 0.25, 0.5, 0.75, etc.
df[df.gt(df.quantile(q=quantile, axis=1), axis=0)].sum(axis=1)
