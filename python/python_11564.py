# How to broadcast on a single index in hierarchically indexed DataFrame?
df['salary'] = series.reindex(df.index, level=0)
