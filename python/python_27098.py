# How to replace every item in a list except last
for l in lists:
    l[:-1] = ['x'] * (len(l) - 1)
