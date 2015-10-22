# top -10 unique dictionary keys to be found on the basis of value
sorted(a.keys(), key=a.get)[:10]
