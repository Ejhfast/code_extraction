# numpy: Replacing values in a recarray
for fieldname in a.dtype.names:
    ind = a[fieldname] == ''
    a[fieldname][ind] = '54321'
