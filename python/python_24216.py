# In Pandas/Numpy, How to implement a rolling function inside each chunk using 2 different columns?
def chunkify(chunk_size):
    df['chunk'] = (df.index.values - 1) / chunk_size
    df['E'] = df.groupby('chunk').apply(lambda x: x.B - pd.expanding_min(x.C)).values.flatten()
