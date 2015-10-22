# How to get statistic of a list of lists in python?
d = defaultdict(int)
for lst in lists:
   d[len(lst)] += 1
