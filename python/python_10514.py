# How do you write a SWIG interface file for a function that uses vector<string>?
%include "stl.i"
%template(_string_list) std::vector&lt; std::string &gt;;
