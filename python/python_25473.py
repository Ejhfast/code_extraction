# pandas - How to save only selected columns of a DataFrame to HDF5
cols_to_keep = ['User_ID', 'Year']
df[cols_to_keep].to_hdf(...)
