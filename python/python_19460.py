# Apply function to a specific number of rows in a DataFrame
df.resample(df.index.freq * 10, how='mean')
