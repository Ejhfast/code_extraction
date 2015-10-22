# Fastest way of deleting certain keys from dict in Python
dict((k, v) for (k, v) in somedict.iteritems() if not k.startswith('someprefix'))
