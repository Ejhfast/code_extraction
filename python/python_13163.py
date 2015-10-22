# python: elegant and code saving way to convert a list
converted = map(tuple, points) # Python 2
converted = list(map(tuple, points)) # or BlackBear's answer for Python 3
converted = [tuple(x) for x in points] # another variation of the same
