# Can I return a list of ALL min tuples, using Python's Min function?
listo = [('a','1'),('b','0'),('c','2'),('d','0')]
minValue = min(listo, key=lambda x: x[1])[1]
minValueList = [x for x in listo if x[1] == minValue]
