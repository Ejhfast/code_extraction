# numpy arrays type conversion in C
PyArrayObject* float_array = (PyArrayObject*)PyArray_FromAny(input,PyArray_DescrFromType(NPY_FLOAT64), 0,0, flags);
