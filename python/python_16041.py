# How to pad till end-of-day in pandas?
series.groupby(pd.TimeGrouper('D')).apply(pd.Series.ffill)
