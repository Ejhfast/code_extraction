# Display a list of user defined functions in the Python IDLE session
import types
print [f for f in globals().values() if type(f) == types.FunctionType]
