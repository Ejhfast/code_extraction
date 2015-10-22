# python: better workaround for treating argument in bash/cmd line as an object
import importlib
path = importlib.import_module('os.path')
print(path.join('a','b'))
