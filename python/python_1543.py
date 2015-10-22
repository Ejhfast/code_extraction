# is there a way to view the source of a module from within the python console?
import module
import inspect
src = inspect.getsource(module)
