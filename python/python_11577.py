# Python reference for hasattr() choices to identify types
from collections import Sequence    # collections.abc in Python 3.3
isinstance(arg, Sequence) and not isinstance(arg, basestring)    # str in Python 3
