# Getting attributes of a Python package that I don't have the name of, until runtime
def get_params(packagename):
    module = __import__('alpha.%s' % packagename)
    return module.__dict__['REQUIRED_PARAMS']
