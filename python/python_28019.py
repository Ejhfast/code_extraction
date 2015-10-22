# Efficient way of removing keys of certain prefix from python dictionary
for k in d.keys():
    if k.startswith('Prefix'):
        d.pop(k)
