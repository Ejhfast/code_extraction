# How to get a 16bit Unsigned integer in python
import struct
struct.unpack('H', struct.pack('h', number))
