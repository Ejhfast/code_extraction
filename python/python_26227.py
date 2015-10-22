# Python - How to copy only new modified files
list(set(os.listdir(dir_src)) - set(os.listdir(dir_dst)))
