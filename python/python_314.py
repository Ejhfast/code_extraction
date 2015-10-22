# Getting the name of the active window
import win32gui
  w=win32gui
  w.GetWindowText (w.GetForegroundWindow())
