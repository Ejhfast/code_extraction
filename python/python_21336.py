# Updating a dataframe with boolean sub-indexing
df.update((df[cols] &gt; 1.2).replace((True, False), (1, np.nan))
