# Deleting elements from dictionary values (lists of list)
newDict = {k : map(lambda x: [x[2], x[3], x[5]], v) for k, v in dict.items() }
