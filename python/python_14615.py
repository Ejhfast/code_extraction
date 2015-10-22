# Conflict using both memory_profiler and docopt
if sys.argv[0].endswith('memory_profiler.py'):
    del sys.argv[0]
