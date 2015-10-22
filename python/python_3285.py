# How do I make a Python script (installed as a service) survive a logout?
win32api.SetConsoleCtrlHandler(lambda x: True, True)
