# How do I make Python 3.4 c_char_array read strings as two bytes?
Cname.raw.decode('utf_16le').rstrip('\x00')
