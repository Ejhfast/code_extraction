# Pythonic way to fetch all elements in a dictionary, falling between two keys?
dict((k,v) for k,v in parent_dict.iteritems() if 2 &lt; k &lt; 4)
