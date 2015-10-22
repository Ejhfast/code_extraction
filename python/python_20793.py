# Merging two DataFrames using an aggregate on a column on one of the DataFrames
A1 = A.groupby('key1').mean().reset_index()
pd.merge(B, A1, on='key1')
