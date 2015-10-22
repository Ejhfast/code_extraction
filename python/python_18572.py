# Python: How to dynamically write to multiple files
d = {1: Logfile1, 2: Logfile2, ...}
curr_file = d[filePointer[0]]
curr_file.write(str(capData[0]))
