# Simulating C#'s sbyte (8 bit signed integer) casting in Python
from ctypes import cast, pointer, c_int32, c_byte, POINTER
cast(pointer(c_int32(arg1)), POINTER(c_byte)).contents.value
