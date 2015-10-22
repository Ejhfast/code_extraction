# PyInstaller failing to include some modules from C:\Python27\Lib
pyinstaller --hidden-import=timeit --hidden-import=bisect -F MyMainModule.py
