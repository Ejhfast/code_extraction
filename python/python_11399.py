# functools.wraps for python 2.4
def partial(func, *args, **kwds):
    "Emulate Python2.6's functools.partial"
    return lambda *fargs, **fkwds: func(*(args+fargs), **dict(kwds, **fkwds))
