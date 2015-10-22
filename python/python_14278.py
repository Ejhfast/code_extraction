# Add new column in pandas dataframe object with column math
grouped = df.groupby([df.index.year,df.index.day])
df['sum'] = grouped.apply(lambda x: x.Open + x.Close)
