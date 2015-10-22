# Comparing lists of lists and writing certain elements into a new list
s = set(x[0] for x in amm)
amv = [x for x in data if x[4] in s]
