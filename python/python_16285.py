# How to find word next to a word in Python
your_string = "This is a string"
list_of_words = your_string.split()
next_word = list_of_words[list_of_words.index(your_search_word) + 1]
