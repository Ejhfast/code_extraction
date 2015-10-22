# Process size in XP from Python
import win32process
print win32process.GetProcessMemoryInfo(win32process.GetCurrentProcess())
