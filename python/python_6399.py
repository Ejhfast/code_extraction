# Having arbitrary number of arguments with a named default in python
def myFunc(*args, **kwargs):
    optDefault = kwargs.pop('optDefault', 1)
    assert kwargs == {}, "There may only be one keyword argument to myFunc"
