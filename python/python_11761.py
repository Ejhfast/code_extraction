# How to use Swig to treat a void * function parameter as Python string
%typemap(in) void* = char*;
