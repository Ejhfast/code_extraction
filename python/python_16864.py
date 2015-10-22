# Create a Python3 module at runtime while initialize an embedded Python
/* Add a built-in module, before Py_Initialize */
PyImport_AppendInittab("xxx", PyInit_xxx);
