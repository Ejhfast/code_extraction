# Pywin32 SendKeys: "Windows button" keypress
import ctypes
ctypes.windll.user32.LockWorkStation()
