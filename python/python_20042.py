# join or merge values calculated on grouped pandas dataframe
df['bins'] = df.groupby(df.hours).density.transform(func)
