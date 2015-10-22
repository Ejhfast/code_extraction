# How to rename a file and preserve creation date in Python
stat = os.stat(myfile)
    // your code - rename access and modify your file
    os.utime(my_new_file, (stat.st_atime, stat.st_mtime))
