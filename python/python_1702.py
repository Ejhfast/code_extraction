# How to convert ip address to DWORD?
struct.pack('bbbb', *(int(x) for x in '127.0.0.1'.split('.')))
