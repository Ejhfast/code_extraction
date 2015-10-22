# possible bug: pandas trying to fill int column with floats
df.loc[df.a==1,'c'] = df['b']
