# coerce() equivalent in python 3
def coerce(x, y):
    t = type(x + y)
    return (t(x), t(y))
