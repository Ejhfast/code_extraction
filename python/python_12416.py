# Passing python class object as parameter to c library
class POINT(Structure):
    _fields_ = [("x", c_int),
               ("y", c_int)]
