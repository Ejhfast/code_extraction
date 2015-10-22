# in Pandas Dataframe, after I set an entire column, I can't update another column with times
df.loc[start,'timenow']= datetime.today()
print df
