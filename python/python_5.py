# Finding what methods an object has
[method for method in dir(object) if callable(getattr(object, method))]
