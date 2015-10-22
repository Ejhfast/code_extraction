# Can I set dataframe values without using iterrows()?
df.C[df.B == 'x'] = df.C.shift(-1)
