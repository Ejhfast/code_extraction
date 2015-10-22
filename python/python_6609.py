# Python C bindings Py_InitModule issue
#define Py_InitModule3(name, methods, doc) \
    Py_InitModule4(name, methods, doc, (PyObject *)NULL, \
                   PYTHON_API_VERSION)
