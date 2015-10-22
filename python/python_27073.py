# How do I find which monitor the mouse pointer is in with python?
from Xlib import display
data = display.Display().screen().root.query_pointer()._data
locationtuple = (data["root_x"], data["root_y"])
