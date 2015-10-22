# Pandas DataFrame merge between two values instead of matching one
a["merge"] = 1
b["merge"] = 1
c = a.merge(b, on="merge")
