# Why does a list slice [:n] allow using a list with fewer than n elements in a loop?
l = range(1,2)
l[:10] == l
