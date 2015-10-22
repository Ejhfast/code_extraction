# Decorators changing arguments to a function
new_args = [arg.upper() for arg in args]
return func(*new_args)
