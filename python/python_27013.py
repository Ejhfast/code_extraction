# Remove prefix from python list objects and single quotes
strList = map( str, objList)
strList = map( lambda x: x.replace( 'Volume:', ''), strList)
