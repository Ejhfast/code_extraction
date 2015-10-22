# Join Recarrays by attributes in Python
dct = dict(zip(data2['causes'], data2['analyst']))
all_data = mlab.rec_append_fields(data1, 'analyst',
    [dct[x] for x in data1['causes']])
