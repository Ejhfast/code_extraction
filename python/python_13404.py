# Reverse indexing a list of lists in Python
for i, x in enumerate(a):
    for j in x:
        b[j].append(i)
