# Creating recursively a function gaining variables each iteration in Python
def f(t, *a):
    return sum(exp(x * t) for x in a)
