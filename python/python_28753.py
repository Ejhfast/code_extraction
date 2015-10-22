# Applying uppercase to a column in pandas dataframe
df['1/2 ID'] = map(lambda x: x.upper(), df['1/2 ID'])
