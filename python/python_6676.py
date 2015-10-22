# update one dictionary with another by adding values rather then replacing it
for key, value in dict2.iteritems():
    dict1.setdefault(key, []).extend(value)
