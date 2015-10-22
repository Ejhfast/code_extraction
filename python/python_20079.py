# Modifying every tuple (and eventually just removing) from a list of tuples
tradeRanges = [(0,3), (10,14), (16,16), (21,23), (25,25)]
print [(n1, n2, abs(n1-n2)) for n1, n2 in tradeRanges if n1 != n2]
# [(0, 3, 3), (10, 14, 4), (21, 23, 2)]
