# Ironpython in C# Import Module Error import csv module
var paths = pyEngine.GetSearchPaths();
paths.Add(@"C:\Program Files (x86)\IronPython 2.7\Lib");
pyEngine.SetSearchPaths(paths);
