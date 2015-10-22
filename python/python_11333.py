# Is this the fastest way to build dict?
ADict = dict((x.get('key'), x.find('A').text) for x in fields)
BDict = dict((x.get('key'), x.find('B').text) for x in fields)
