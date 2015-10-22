# Printing negative values as hex in python
for x in range(-4,5):
   print "hex x %d 0x%08X" % (x, x &amp; 0xffffffff)
