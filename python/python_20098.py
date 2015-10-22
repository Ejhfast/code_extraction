# Sort list after numerical value in string
words_list = ["Bluebird, 4005", "ABCD, 1", "EFGH, 2677", "IJKL, 2"]
print sorted(words_list, key = lambda x: int(x.split(",")[1]))
# ['ABCD, 1', 'IJKL, 2', 'EFGH, 2677', 'Bluebird, 4005']
