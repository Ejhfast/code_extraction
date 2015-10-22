# Pandas: Querying an object column in dataframe
df[df['Q2'].apply(lambda x : 1 in x)]
