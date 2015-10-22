# How to check if variable is string with python 2 and 3 compatibility
from six import string_types
isinstance(s, string_types)
