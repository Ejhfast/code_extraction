# Best Way to add group totals to a dataframe in Pandas
df['TotalCount'] = df.groupby('Group')['Count'].transform(sum)
