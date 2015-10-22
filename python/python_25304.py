# Python cannot load file
words_file = askopenfile(mode='r', title='Select word list file')
words = a3.read_words(words_file)
words_file.close()
