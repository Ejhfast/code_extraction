# How to get the absolute path of a file using tkFileDialog?
file = tkFileDialog.askopenfile(parent=root,mode='rb',filetypes=[('Subrip Subtitle File','*.srt')],title='Choose a subtitle file')
abs_path = os.path.abspath(file.name)
