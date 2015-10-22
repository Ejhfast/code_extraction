# How do you know the frequency of each letters?
import string
all_words = 'this is me'
print("there is:\n {0}".format('\n'.join([letter+':'+str(all_words.count(letter) + all_words.count(letter.lower())) for letter in string.uppercase])))
