# Subsetting data in pandas with complex operations
criterion = df['year_week'].map(lambda x: len(x)&lt; 6)
df[criterion].index.values
