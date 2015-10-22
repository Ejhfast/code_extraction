# How to convert a binary representation of a string back to the original string in Python?
import binascii
n = int('0110100001101001001000000111010101110011', 2)
binascii.unhexlify('%x' % n)
