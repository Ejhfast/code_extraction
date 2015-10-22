# Slice pandas dataframe in groups of consecutive values
for k,g in df.groupby(df['A'] - np.arange(df.shape[0])):
    print g
