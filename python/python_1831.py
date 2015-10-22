# How can I get the window focused on Windows and re-size it?
import win32gui
hwnd = win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd, 0, 0, 500, 500, True)
