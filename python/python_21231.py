# Drop columns from pandas dataframe, regardless of whether ALL column names are present
df.drop(set(drop_list) &amp; set(df.columns), axis=1)
