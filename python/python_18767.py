# Python: print incomplete
print('\n'.join('{}: {} ({})'.format(*k) for k in sorted(usinlist, key=lambda k: (k[2], k[0], k[1]))))
