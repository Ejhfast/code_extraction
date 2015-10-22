# Checking for interactive shell in a Python script
import os, sys
if os.isatty(sys.stdout.fileno()):
    ...
