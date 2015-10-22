# Calling a Python function from a C thread, with a mutable C array
PyObject *array = PyObject_CallFunction(array_type, "c", 'd');
