# How to check for a letter in raw_input
word = raw_input("Enter the magic word:")
word = word if word.startswith('b') else 'b' + word
print "your magic word is %s" % (word)
