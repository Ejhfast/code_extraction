# Is there something like python's issubclass which will return False if the first arg is not a Class?
import inspect
def isclassandsubclass(value, classinfo):
    return inspect.isclass(value) and issubclass(value, classinfo)
