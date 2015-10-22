# Making a single decorator of out multiple
def both_decorators(func):
    return decorator1(decorator2(func))
