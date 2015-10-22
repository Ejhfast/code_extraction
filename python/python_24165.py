# Create a pandas dataframe column based on a logical test
df1 = df[df['ccy1'] &gt;= df['ccy2']]
df2 = df[df['ccy1'] &lt; df['ccy2']]
