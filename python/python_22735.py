# Return_value_policy for method with void return type and optional parameter
def("method", &amp;A::method, (arg("par1"), arg("par2") = false))
