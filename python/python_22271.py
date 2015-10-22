# Python pandas join on with overwrite
df = df[df.columns[df.columns!='values']].join(s, on='keys')
