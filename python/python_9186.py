# Python: Get Folder containing specific files extension
set(folder for folder, subfolders, files in os.walk('/') for file_ in files if os.path.splitext(file_)[1] == '.png')
