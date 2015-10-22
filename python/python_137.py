# How can I dynamically get the set of classes from the current python module?
import sys
getattr(sys.modules[__name__], 'A')
