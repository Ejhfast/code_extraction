# Getting a path from the User with Tkinter
dirOpts = { 'initialdir': '/', 'mustexist': True, 'title': 'MyFileDialog' }
dirName = tkFileDialog.askdirectory(**dirOpts)
