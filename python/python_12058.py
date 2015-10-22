# How can I install Python modules programmatically / through a Python script?
from setuptools.command import easy_install
easy_install.main( ["pythonModule"] )
