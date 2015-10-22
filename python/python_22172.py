# Set a global variable with eval or exec in Python
def setglobal(s, x):
    globals()[s] = x
