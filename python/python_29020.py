# Remove line from dataframe based on date comparison
df2 = df2[(df2['CurrentDate']) &lt;= (df2['EndTime'])]
