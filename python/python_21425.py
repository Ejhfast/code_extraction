# How to sort by mtime a given list of files in Python3?
sorted_list = sorted(lista, key=lambda f: os.stat(f).st_mtime)
