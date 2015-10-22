# Error loading dll in path with parenthesis using ctypes (python)
os.chdir(r"C:\Program Files(x86)\SomeFolder")
 the_dll = WinDLL("SomeDLL.dll")
