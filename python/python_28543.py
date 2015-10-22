# Python: group list items in a dict
res = {}
for item in l:
    res.setdefault(item['a'], []).append(item)
