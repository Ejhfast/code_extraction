# Python Pandas Replacing column names
dataset.rename(columns={typo: 'Address' for typo in AddressCol}, inplace=True)
