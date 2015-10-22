# getting aggregates of aggregates in pandas
df.groupby('somecol')[fieldList].agg(np.mean).describe()
