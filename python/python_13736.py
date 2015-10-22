# Reading from file a hierarchical ascii table using Pandas
r=pd.read_fwf('test.txt', widths=(3, 8, 9, 14, 14, 14),skiprows=1, header=None)
r=r.fillna(method='pad')
r=r.set_index(['X0','X1','X2'])
