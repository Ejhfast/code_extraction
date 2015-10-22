# When using dataframes as params for .fillna(), is identical shape required?
df1.fillna(df1.groupby(level=0).transform("mean"))
