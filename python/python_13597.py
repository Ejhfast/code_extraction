# python : convert string to c_ubyte_Array_8
(ctypes.c_ubyte * 8)(*[ctypes.c_ubyte(ord(c)) for c in str[:8]])
