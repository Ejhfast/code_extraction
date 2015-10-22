# How to create a function with both default and arbitrary arguments
def defaultsAndArbitrary(arr, *modifiers, **kwargs):
    example1 = kwargs.get('example1',True)
    example2 = kwargs.get('example2',13)
