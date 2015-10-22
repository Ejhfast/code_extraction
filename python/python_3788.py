# Sorting alphanumerical dictionary keys in python
keys.sort(key=lambda k:(k[0], int(k[1:])) )
