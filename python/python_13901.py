# pandas combine multiple dataframes or use as updates
df = df1.reset_index().merge(df2.reset_index(), on=['index','cols']).set_index('index')
