# Faster way to transform group with mean value in Pandas
pd.Series(np.repeat(grp.mean().values, grp.count().values))
