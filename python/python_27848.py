# I've got a CPython C++ module with C++11 code, but I can't seem to build on travis-ci
install:
  - sudo apt-get install -qq gcc-4.8 g++-4.8
  - CC=g++-4.8 python setup.py install
