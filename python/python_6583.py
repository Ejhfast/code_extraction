# efficiently turning a ctypes LP_c_ubyte into a python 'str'
import ctypes
pp = ctypes.string_at(msg.payload, msg.payloadlen)
