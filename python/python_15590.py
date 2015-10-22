# Sort list of objects by attribute alphanumerically
sorted(obj, key=lambda x: (x.name[0], int(x.name[1:])))
