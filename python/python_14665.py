# How to iterate through dict values containing lists and remove items?
d = {k:[elem for elem in v if not elem.endswith(')')] for k,v in d.iteritems()}
