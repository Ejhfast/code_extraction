# Bitmask parsing in python using only standard library
size = 8
[bool(235 &amp; (1 &lt;&lt; size - i - 1)) for i in xrange(size)]
