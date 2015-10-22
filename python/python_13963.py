# How to use Python left outer join using FOR/LIST/DICTIONARY comprehensions (not SQL)?
d2 = dict(t2)
res = [[k[0], d2.get(k[0], 0)] for k in t1]
