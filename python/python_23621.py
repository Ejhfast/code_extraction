# Cannot convert from unicode
var = [tuple(s.encode('ascii', 'replace') for s in t) for t in var]
