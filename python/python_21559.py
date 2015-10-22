# How can I pass a single PyObject (created in a C++ backend) to an embedded Python Interpreter?
pValue = PyObject_CallMethodObjArgs(VM, pFunc, pNoddy, NULL);
