# "python way" to parse and conditionally replace every element in 2D list
for single_list in myLists:
    for i, item in enumerate(single_list):
        single_list[i] = numParser(item)
