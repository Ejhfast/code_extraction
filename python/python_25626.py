# efficient way to find last time stamp for each unique value in a column in HDF5 table
store.select(asset, where = Tag = ['" + tag + "'] &amp; columns ['Datetime']")).tail(1)
