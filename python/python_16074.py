# Cocatenating strings in place in a dictionary
for stuff in listofstrings:
    dictionary["key"] = dictionary.get("key",defaultvalueforkey) + stuff
