# KDB+ like asof join for timeseries data in pandas?
df1.apply(lambda x: x.asof(df2.index))
