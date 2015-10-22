# Subsetting a dataframe using column sum in Python
df2 = df1.drop(df1.columns[df1.sum() &gt;= 100], axis=1)
