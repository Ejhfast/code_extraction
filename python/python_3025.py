# Special type of combination using itertools
k = int(raw_input('From What row items should be appeared again at the end?'))
res = [l for l in product(*(li+[li[k]])) if l[k]&lt;l[len(li)] ]
