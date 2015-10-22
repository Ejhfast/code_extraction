# Joining 2 dataframes on a specific column with IDs
pd.merge(df1, df2, on='record_ID', how='left')
