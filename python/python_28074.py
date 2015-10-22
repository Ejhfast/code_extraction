# How to filter a pandas DataFrame for a certain column value and only return columns that do not have NAN?
dt[dt['year']==2001].dropna(axis=1)
