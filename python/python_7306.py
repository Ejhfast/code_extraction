# Using msvcrt in 64-bit python ctypes
libc.fopen.restype = ctypes.c_void_p
fp = libc.fopen(...)
libc.fclose(fp)
