# Merging and Filling in Pandas DataFrames
df_together = pd.concat([df1, df2]).groupby('key').max()
