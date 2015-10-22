# Handling Pandas dataframe columns with mixed date formats
df1['DateTime']=pd.to_datetime(df1['Time_Date'],coerce=True)
nulls=df1['Time_Date'][df1['Time_Date'].notnull()==False]
