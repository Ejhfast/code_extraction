# PyRun_String stop sending result to stdout after any error
PyRun_String(line, Py_single_input, py_dict, py_dict);
PyRun_SimpleString("\n");
