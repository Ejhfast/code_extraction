# convert dictionary key and value to unicode
d = {'firstname' : 'Foo', 'lastname' : 'Bar'}
d = {unicode(k):unicode(v) for k,v in d.items() }
