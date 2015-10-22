# Python intersection of datetimes from multiple lists/dictionaries
var = {}
for set, list in records.iteritems():
    var[set] = [i['Time Stamp'] for i in list]
