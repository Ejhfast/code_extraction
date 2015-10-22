# python pandas dataframe join two dataframes
df.merge(df2,how='outer',left_on=['ID','COUNTRY','YEAR'],right_on=['ID',"COUNTRY","YEAR"])
