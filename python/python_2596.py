# Retrieving the Return Value of a Stackless Python Tasklet Bound Function?
def RunFunctionAndGetResult(chan, func, *args, **kwargs):
      chan.send(func(*args, **kwargs))
