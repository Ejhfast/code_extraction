# Loading c dll in python
PySys_SetPath(".");
mymod = PyImport_ImportModule("your_DLL_name or Py_module_name");
