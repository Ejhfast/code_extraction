# Merge pandas dataframe, with column operation
df3 = pd.concat([df1, df2], join = "outer", axis=1)
df4 = df3.b.sum(axis=1)
