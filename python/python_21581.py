# Python Subprocess causing latency with shell
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
shellreturn = subprocess.check_output(["C:\Python34\python", root.wgetdir + "\html2text.py", keyworddir + "\\" + item], startupinfo=startupinfo) #this could be any subprocess.
