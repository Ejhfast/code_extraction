# Auto fill np.nan for arrays of different size
d = {"a":[1,2,3],"b":[1,2], "c":[1]}
pd.concat(map(pd.Series, d.values()), keys=d.keys(), axis=1)
