# Automatically find files that start with similar strings (and find these strings) using Python
names = set([name.rpartition('_')[0] for name in glob('*_*.dat')])
