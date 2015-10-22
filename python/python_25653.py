# Python default values for tuple in function arguments
def func(self, args):
    defaultargs = (1, 2, 3)
    args = tuple(map(lambda x, y: y if y is not None else x, defaultargs, args))
