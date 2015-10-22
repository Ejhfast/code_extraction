# Best way to joint list of list horizontly
result = [[x for inner in middle for x in inner] for middle in list_of_lists]
