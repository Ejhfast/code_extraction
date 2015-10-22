# Efficient way to reuse pre-built dictionary if data is redundant? Deepcopy is too slow
newdict = {k, v[:] for k, v in olddict.iteritems()}
