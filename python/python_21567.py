# Use python next() in for loop without advancing the for loop
for word, next_word in zip(words[:-1], words[1:]):
    print word
    checknextword = next_word
