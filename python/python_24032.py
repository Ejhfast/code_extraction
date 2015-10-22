# Python: using "__getattr__" without a class?
import sys
current_module = sys.modules[__name__]
getattr(current_module, 'AFunction')
