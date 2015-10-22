# Adding means to a pandas dataframe
df2 = df.stack().unstack(-2)
df2["mean"] = df2.mean(axis=1)
