# How do I check for type equality (is operator or x.GetType() == typeof(xType)) in IronPython?
from System import *
if x.GetType() == Type.GetType(xType):
