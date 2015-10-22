# How to group related .tif files?
grouped = [list(g) for _, g in itertools.groupby(test, lambda x: x.split('_')[2])]
