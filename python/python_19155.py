# Django: Getting a Model type when Using a Defer Query
t = type(obj)
if t._deferred:
  t = t.__base__
