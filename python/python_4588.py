# random number generator in boost.python
boost::python::object randmod = boost::python::import("numpy.random")
boost::python::object randfunc = randmod.attr("RandomState")
randfunc(10)
