# Python, make filename based on path and replace backslash
import os
out='a/b/c/'.replace(os.path.sep, '_')
print out
