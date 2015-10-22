# In python, how to store 'constants' for functions only once?
def foo(bar):
    return foo.my_map.get(bar, defaultType)()
foo.my_map = {"rab": barType, "oof": fooType}
