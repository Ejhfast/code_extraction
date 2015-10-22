# How to get the first 11 bits of a 32 bit int with ctypes
class Fields(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('x', ctypes.c_uint, 21), ('a', ctypes.c_uint, 11)]
