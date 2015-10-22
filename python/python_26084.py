# How to default to the default argument in Python
kwargs = dict((k, getattr(self, k)) for k in ('c', 'd') if getattr(self, k))
print_something(a, b, **kwargs)
