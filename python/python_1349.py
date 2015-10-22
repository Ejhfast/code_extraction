# How would I call 32bit exes in Windows 64bit with python?
textEditorExecutablePath = 'C:\\Program Files (x86)\\Notepad2\\Notepad2.exe'
filepathToOpen = 'C:\\file.txt'
subprocess.Popen([textEditorExecutablePath, filepathToOpen])
