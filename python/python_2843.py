# from ... import * with __import__ function
_temp = __import__(name, globals(), locals(), [name_of_class]); your_class = _temp.name_of_class
