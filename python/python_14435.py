# HDFStore Exception: cannot find the correct atom type : a basic case
df['datetime64'] = Series(df['datetime64'],dtype='M8[n2]')
