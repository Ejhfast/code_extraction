# Modifying a subset of rows in a pandas dataframe
df.ix[df.A==0, 'B'] = np.nan
