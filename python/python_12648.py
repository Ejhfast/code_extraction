# Write an array of differing lengths to a csv in python
for i in range(len(t)):
    row = [[ e.a, e.b, e.c, ...] + [e.z[0], e.z[1], e.z[2], ...] for e in t[i]]
    t.writerow(row)
