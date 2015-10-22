# Creating an IronPython (dynamic) object from a string
var engine = Python.CreateEngine();
dynamic calculator = engine.CreateScope();
engine.Execute(GetPythonScript(), calculator);
