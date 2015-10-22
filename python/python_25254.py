# how do I close window with handle using win32gui in Python
import win32con
win32gui.PostMessage(handle,win32con.WM_CLOSE,0,0)
