# Extract substring from string in dataframe
df['ticker'] = df['Company Name'].str.extract("\((.*)\)")
