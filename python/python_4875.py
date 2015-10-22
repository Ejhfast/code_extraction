# Export variable into python from C++ using boost.python
boost::python::scope().attr("Pi") = Pi;
