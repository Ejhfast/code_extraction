# Python reference count and ctypes
clib = ctypes.cdll.LoadLibrary('some.so')
c_foo = clib.c_foo
c_foo.restype = ctypes.py_object
