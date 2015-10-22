# How to create a checksum of a file in python
import hashlib
[(fname, hashlib.md5(open(fname, 'rb').read()).digest()) for fname in fnamelst]
