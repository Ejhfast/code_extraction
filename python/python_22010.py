# Subtracting a string from a string in a Python Pandas dataframe
mask = (df['date'] - df['item1 birth'] &lt;= 3)
df2 = df.loc[mask]
