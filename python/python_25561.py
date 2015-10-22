# Select column based on condition on other column, vectorized, pandas
df["new"]=np.nan
df["new"][df["C"]=='a']=df["A"]
df["new"][df["C"]=='b']=df["B"]
