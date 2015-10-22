# Define array type in Python to be filled by C function
out_char = ctypes.c_char()
result = lib.test(ctypes.byref(out_char))
