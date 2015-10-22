# Python: Check for unique characters on a String
word = raw_input()
reduced_word = ''.join(
    [char for index, char in enumerate(word) if char not in word[0:index]])
