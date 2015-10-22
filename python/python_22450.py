# Converting groupby dataframe (with dropped duplicate rows by group) into normal dataframe
df4 = df3.drop_duplicates(['Organization', 'Name'])
