# TypeError:exceptions must be old-style classes or derived from BaseException, not str
test = 'abc'
if True:
    raise Exception(test + 'def')
