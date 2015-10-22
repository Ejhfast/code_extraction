# grabbing the file description from details tab
langs = win32api.GetFileVersionInfo(ExecutablePath, r'\VarFileInfo\Translation')
key = r'StringFileInfo\%04x%04x\FileDescription' %(langs[0][0], langs[0][1])
print (win32api.GetFileVersionInfo(ExecutablePath, key))
