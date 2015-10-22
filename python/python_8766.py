# Unspecified byte lengths in Python
version, type, length = struct.unpack("cch", packed[:4])
content, = struct.unpack("%ds" % length, packed[4:])
