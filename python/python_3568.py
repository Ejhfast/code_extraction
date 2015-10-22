# auto collect information in sub_modules when import in python?
import inspect
import sys
inspect.getmembers(sys.modules[__name__], inspect.isfunction)
