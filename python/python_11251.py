# Efficient way to remove keys with empty values from a dict
dict((k, v) for k, v in metadata.iteritems() if v)
