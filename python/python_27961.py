# How to test both Python and C++ in one .travis.yml without running the C++ multiple times?
script:
  - python setup.py test
  - if [[ $TRAVIS_PYTHON_VERSION == '3.4' ]]; then (cd src &amp;&amp; CC=gcc-4.8 CXX=g++-4.8 make -f Makefile-custom test); fi
