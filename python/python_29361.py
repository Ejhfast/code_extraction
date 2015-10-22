# Is there a way to do cumulative np.bitwise_or in pandas groups?
df.groupby(k).agg(lambda x: np.bitwise_or.reduce(x.values))
