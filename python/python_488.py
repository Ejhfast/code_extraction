# Logout or switch user in Windows using Python
import ctypes
ctypes.windll.user32.LockWorkStation ()
