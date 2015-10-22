# How to convert PyObject to java boolean type
PyObject obj = interpreter.eval("True");
boolean i = ((PyInteger) obj).asInt() != 0;
