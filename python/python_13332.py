# Extract file size and the date when the file is created in Python/Django?
command  = "drwxr-xr-x 4,096 2013/01/20 22:37:39 files".split()
filesize = command[1]
date = command[2]
