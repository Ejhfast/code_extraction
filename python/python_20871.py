# Joining 2 data frames with overlapping data
df = df.reindex(columns=df2.columns.union(df.columns),
                index=df2.index.union(df.index))
