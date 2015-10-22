# clean C++ extension build directory in setup.py
import sys, shutil
if 'clean' in sys.argv:
    shutil.rmtree('cxxextension/build')
