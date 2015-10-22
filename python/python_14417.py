# python exercise help space in for loop
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
print [b+'+'+g for b in boys for g in letterGirls[b[0]]]
