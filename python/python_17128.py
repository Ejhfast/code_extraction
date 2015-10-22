# How to get the name of a function (plus its module) in Python?
def get_fun(fn):
    return '.'.join([fn.__module__, fn.__name__])
