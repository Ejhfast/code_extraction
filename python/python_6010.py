# Make a py2exe exe run without a console?
from distutils.core import setup
import py2exe
setup(windows=["script.py"])
