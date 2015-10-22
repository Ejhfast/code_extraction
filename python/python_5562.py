# Python: How to read a (static) file from inside a package?
import os, mypackage
template = os.path.join(mypackage.__path__[0], 'templates', 'temp_file')
