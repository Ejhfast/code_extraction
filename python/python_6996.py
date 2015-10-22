# boost-python select between overloaded methods
void (Foo::*m1)(A&amp;) = &amp;Foo::m1;
boost::python::class_&lt;Foo&gt;("Foo")
    .def("m1", m1)
