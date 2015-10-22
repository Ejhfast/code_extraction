# chunk_split in python
chunk_split = lambda s: '\r\n'.join(s[i:min(i+76, len(s))] for i in xrange(0, len(s), 76))
