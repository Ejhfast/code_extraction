# Python 2.7.6 Optimizing code for packing big endian bytes into a string
values = [varA[name]['value'] for name in 'ZYXWV']
varC = struct.pack('&gt;'+str(len(values))+'h', *values)
