# How do I convert a Python list into a C array by using ctypes?
import ctypes
arr = (ctypes.c_int * len(pyarr))(*pyarr)
