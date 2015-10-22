# Determine if current user is in Administrators group (Windows/Python)
import ctypes
print ctypes.windll.shell32.IsUserAnAdmin()
