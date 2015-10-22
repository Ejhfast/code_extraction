# Encoding data of mixed type?
[x.encode('latin-1') if isinstance(x, unicode) else x
 for x in row]
