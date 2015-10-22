# How to unpack 6 bytes as single integer using struct in Python
def unpack48(x):
    x1, x2, x3 = struct.unpack('&lt;HHI', x)
    return x1, x2 | (x3 &lt;&lt; 16)
