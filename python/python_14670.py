# program closes when PyEval_CallObject is called
gstate = PyGILState_Ensure();
PyEval_CallObject(inactivity_callback, arglist);
PyGILState_Release(gstate);
