# Using python's pack with arrays
data = pack('&gt;i', len(arr)) + arr.tostring()
