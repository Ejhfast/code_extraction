# Get signal names from numbers in Python
import signal
dict((k, v) for v, k in reversed(sorted(signal.__dict__.items()))
     if v.startswith('SIG') and not v.startswith('SIG_'))
