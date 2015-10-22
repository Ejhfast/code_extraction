# Split a python list into other "sublists" i.e smaller lists
chunks=[data[x:x+100] for x in xrange(0, len(data), 100)]
