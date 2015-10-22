# How can you programmatically tell the CPython interpreter to enter interactive mode when done?
import os
os.environ["PYTHONINSPECT"] = "1"
