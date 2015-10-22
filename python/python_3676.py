# How to use pythons map with a non-iterable and iterable set of parameters?
map(lambda x: callable(getattr(object, x)), dir(object))
