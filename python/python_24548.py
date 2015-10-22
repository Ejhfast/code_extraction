# pandas python: access row by case insensitive label
df[pd.Series(df.index).str.contains('base', case=False)]
