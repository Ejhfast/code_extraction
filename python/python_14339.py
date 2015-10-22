# How to use dtype to structure 1D array in numpy
raw = np.loadtxt(StringIO(a), dtype='f8')
resh = raw.reshape(-1,2) # This will work for any (even) length initial data
rec = resh.view([('x', 'f8'), ('y', 'f8')], np.recarray)
