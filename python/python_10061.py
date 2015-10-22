# python passing a variable to an object property or method through a function argument
def some_function(arg, property):
    return getattr(Some_Object, propery)
