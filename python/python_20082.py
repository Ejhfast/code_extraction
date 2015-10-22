# Finding longest path in a dictionary in python
print max((l[1], l[0], k) for k in d for l in d[k])
# (5.0, 'C', 'A')
