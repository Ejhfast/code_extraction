# Script to unpack python 2.7 at bootstrap on amazon EMR node
tar xvf mypython.tar /myapp/python/
export PATH=/myapp/python/:$PATH
export PYTHONHOME=/myapp/python
