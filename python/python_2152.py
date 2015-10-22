# Windows is not passing command line arguments to Python programs executed from the shell
[HKEY_CLASSES_ROOT\Applications\python.exe\shell\open\command]
@="\"C:\\Python25\\python.exe\" \"%1\" %*"
