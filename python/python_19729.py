# Why does Python 2.7 sign extend HDC returned from GetDC() on x64?
from ctypes import *
windll.user32.GetDC.restype = c_void_p
hDC1 = windll.user32.GetDC(None)
