# How can I print the type of a PyObject in an error message for an embedded Python script?
PyTypeObject* type = key-&gt;ob_type;
const char* p = type-&gt;tp_name;
std::cout &lt;&lt; "My type is " &lt;&lt; p &lt;&lt; std::endl;
