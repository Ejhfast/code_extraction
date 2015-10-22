# What is the most pythonic way to conditionally return a function
def func2(n):
    ret = func1(n)
    return ret if ret is not None else something_else
