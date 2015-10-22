# Send Key Event to a Child Window
import win32api
   win32api.PostMessage(handler, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
