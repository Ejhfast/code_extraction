# Python: How do I get a reference to a module inside the module itself?
import sys
current_module = sys.modules[__name__]
