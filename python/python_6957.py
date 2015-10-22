# Python: finding whether a string starts with one of a list's variable-length prefixes
name=name[len(filter(name.startswith,prefixes+[''])[0]):]
