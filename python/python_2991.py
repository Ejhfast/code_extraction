# IP address conversion using Python
''.join([ bin(int(x))[2:].rjust(8,'0') for x in '123.123.123.123'.split('.')])
