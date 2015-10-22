# HDFStore select_as_multiple generator
for df in store.select('df',chunksize=10000):
    print df
