# lambda function to convert dict to string as a lambda expression in python
dict_to_str = lambda x: ','.join("%s:%s" % (str(k), str(v)) for (k, v) in x.iteritems()) if isinstance(x, dict) else x
