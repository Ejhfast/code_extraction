# How to construct a Complex from a String using Python's C-API?
PyObject *c1 = PyObject_CallFunction(PyComplex_Type, "s", "1+2j");
If (!c1)
  return NULL;
