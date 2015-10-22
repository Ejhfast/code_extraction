# Sequential within-group enumeration in Pandas
df['date_indexer'] = df.groupby('date').cumcount()
