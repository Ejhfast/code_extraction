# Killing the background window when running a .exe from a Python program
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
p = subprocess.Popen(args = "demo.exe", stdout=subprocess.PIPE, startupinfo=startupinfo)
