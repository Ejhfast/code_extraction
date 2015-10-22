# Compiling Python project in C++. How do I include linked library
g++ -shared python/swig_wrap.o  -IC:/Python27/include/ -LC:/Python27/libs -lpython27 -o python/_lib.so
