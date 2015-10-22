# create a boost::python::object from a noncopyable instance
boost::python::object obj(**boost::cref(a)**);
