# Trying to pass parameters as functions in Python
def sort(sortlist, sortby):
    sortlist.sort(key = lambda x: getattr(x, sortby))
