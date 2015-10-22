# Find top-level directory from subdirectory on Linux in Python
import os.path
print os.path.abspath(__file__+'/../../..')   # the directory three levels up
