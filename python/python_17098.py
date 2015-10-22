# Count elements in nested list
[sum([x.count(1) for x in L[:i]]) for i in range(1, len(L) + 1)]
