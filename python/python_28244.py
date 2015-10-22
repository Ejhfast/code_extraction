# Disable cmd opening from GUI (PyQt)
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
return subprocess.Popen([command] + args, startupinfo=startupinfo).wait()
