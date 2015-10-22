# String format alignment
for i,n in sorted(counter.items()):
    binrange='{}-{}'.format(i*10, (i + 1) * 10 - 1)
    print('{:&lt;12}{:&lt;4}'.format(binrange, n))
