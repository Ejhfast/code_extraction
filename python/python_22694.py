# Write a hex string as binary data in Python
import binascii
hexstr = 'FF0000FF'
binstr = binascii.unhexlify(hexstr)
