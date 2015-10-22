# Call python method from java
interpreter.exec("from test import tmp");
PyObject someFunc = interpreter.get("tmp");
