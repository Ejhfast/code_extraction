# Concatenating Multiple DataFrames with Non-Standard Columns
data=pd.concat(datalist,join='outer', axis=0, ignore_index=True)
