# reading a file and getting each line of the file separately
with open(sys.argv[1]) as f:
  L1, L2, L3 = (line.rstrip() for line in f.readlines()[:3])
