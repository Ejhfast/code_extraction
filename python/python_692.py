# How to test if a class attribute is an instance method
def hasmethod(obj, name):
    return hasattr(obj, name) and type(getattr(obj, name)) == types.MethodType
