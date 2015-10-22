# How do I import non namespaced types into IronPython?
import clr
clr.AddReference("MyAssembly")
import MyGlobalClass
