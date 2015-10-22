# dropping duplicates randomly
idx = np.random.permutation(np.arange(len(df)))
df.iloc[idx].drop_duplicates()
