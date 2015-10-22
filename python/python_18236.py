# xrange not adhering to start, stop, step
with open(sys.argv[1], 'r') as f:
  for _ in xrange(0, 7, 1):
    print f.next().rstrip()
