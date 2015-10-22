# Embedding Python in C, linking fails with undefined reference to `Py_Initialize'
gcc  embedpy.o $(/usr/bin/python2.7-config --ldflags)
