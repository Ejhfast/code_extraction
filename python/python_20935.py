# Combine values from arbitrary number of columns into new one
df.fillna('').sum(axis=1).replace('', np.nan)
