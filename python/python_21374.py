# Pandas modify column values in place based on boolean array
df['flag'][df.name.str.contains('e$')] = 'Blue'
