# Python Pandas - Re-ordering columns in a dataframe based on column name
df.reindex_axis(sorted(df.columns), axis=1)
