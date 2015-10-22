# Differences between the following python and ruby code
for x in range(1, 13):
    print ''.join([format(x * y, '2d' if y == 1 else '4d')
                   for y in range(1, 13)])
