# Python: File IO - Disable incremental flush
a = open("blah.txt", "w", 2 ** 31 - 1)
for i in xrange(10000):
    a.write("a")
