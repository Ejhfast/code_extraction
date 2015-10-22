# Interleave list with fixed element
[elem for x in list for elem in (x, 0)][:-1]
