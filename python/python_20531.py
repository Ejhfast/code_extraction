# Split a list into sub lists in python
result = [my_list[idx:idx + 3] for idx in range(0, len(my_list), 3)]
# [['text1', 'text1', 'text1'],
#           ['text2', 'text2', 'text2'], ['text3', 'text3', 'text3']]
