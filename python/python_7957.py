# How to invoke a external application(Windows based) independent of parent python script?
import win32api
win32api.ShellExecute(0, "open", "python.exe", 'blah.py', '', 1)
