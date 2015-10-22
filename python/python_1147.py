# How can I pass a function's name to a function, and then call it?
def outer(f):          # any name: function, class, any callable
    return f()         # class will be instantiated within the scope of the function
