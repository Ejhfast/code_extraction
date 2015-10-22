# Default parameter value for objects
def f(x=list):
    if isinstance(x, type): x = x()
    print(id(x))
