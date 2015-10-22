# Python: How to get the text label from another program window?
buffer = win32gui.PyMakeBuffer(255)
length = win32gui.SendMessage(control, win32con.WM_GETTEXT, 255, buffer)
