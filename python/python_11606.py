# In Python, why doesn't an import in an exec in a function work?
def test():
    exec (code, globals())
    f()
