# How to list a folder's files using the zipfile module in Python
dirfiles = [f for f in z.namelist() if f.startswith(pathprefix)]
