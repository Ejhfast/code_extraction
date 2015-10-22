# automatically resolve numpy recarray
for name in duV.dtype.names:
    globals()[name.lower()] = duV.field(name)
