# Iterate the classes defined in a module imported dynamically
dict([(name, cls) for name, cls in mod.__dict__.items() if isinstance(cls, type)])
