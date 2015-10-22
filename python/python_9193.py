# How do I use my own loop with pyhook instead of pumpMessages()?
import ctypes
ctypes.windll.user32.PostQuitMessage(0)
