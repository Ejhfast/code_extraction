# How to display all words that contain these characters?
for word in file('myfile.txt').read().split():
    if 'x' in word and 'z' in word:
        print word
