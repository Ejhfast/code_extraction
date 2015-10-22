# Get the Key correspond to max(value) in python dict
maxval = max(dict.iteritems(), key=operator.itemgetter(1))[1]
keys = [k for k,v in dict.items() if v==maxval]
