# Python how to sort a dictionary by value in reverse order
d = dict(red=2, blue=45, green=100)
sorted(d.items(), cmp=lambda a,b: cmp(a[1], b[1]), reverse=True)
