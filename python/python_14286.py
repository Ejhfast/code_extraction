# How to trouble-shoot HDFStore Exception: cannot find the correct atom type
store = pd.HDFStore('test0.h5','w')
In [31]: for chunk in pd.read_csv('Train.csv', chunksize=10000):
   ....:     store.append('df', chunk, index=False, data_columns=True)
