# how to groupby hours/days
df.resample('1H', how=lambda x: (x[-1] - x[0]) / (df[-1] - df[0]))
