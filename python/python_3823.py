# Decomposition and decoding of nested dictionary/json
outputdata = {}
for id, stuff in jsonData.iteritems():
    outputdata[id.encode("ascii")] = stuff[u"name"]
