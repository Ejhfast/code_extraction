# Unexpected KeyError Pandas while trying to aggregate multiple functions
test1.groupby("p.sector").agg({'p.pfwt': np.sum})
