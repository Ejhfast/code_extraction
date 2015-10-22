# Python C++ extension with SWIG - calling a function by importing module
%init %{
    my_init_function();
%}
