# Print out the index of a map function
for i,s in map(lambda n: (n,(n*(n+1))/2), range(1,101)):
    print "sum of the first %d integers: %d" % (i,s)
