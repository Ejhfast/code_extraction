# Convert Python byte to "unsigned 8 bit integer"
import struct
value = struct.unpack('B', data[0])[0]
