# retrieve a `char *` returned from C function exported from .so in Python
ctypes.c_char_p( liba.say_hi() )
