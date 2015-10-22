# How can I add each word in a .txt file to a list in Python?
with open('words.txt', "r") as word_list:
    words = word_list.read().split(' ')
