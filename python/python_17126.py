# IPython + Pandas Can't plot data from .csv
df = df.replace(',', '', regex=True)
df = df.replace('-', 'NaN', regex=True).astype('float')
df.plot()
