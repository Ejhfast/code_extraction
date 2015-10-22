# Unpacking an unspecified amount of variables
listMult = [sum(x*y for x, y in zip(tup, somelist)) for tup in tuplelist]
