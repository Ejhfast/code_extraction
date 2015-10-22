# Using cython .pxd files to Augment pure python files
cdef class A:
    cpdef foo(self, int i=*, x=*)
