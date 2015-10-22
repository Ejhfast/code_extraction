# does python will free the memory if I delete a string reference?
op = (PyStringObject *)PyObject_MALLOC(sizeof(PyStringObject) + size);
