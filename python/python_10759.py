# Adding 2 dictionary entries from one string
text = "Yes: No Maybe: So"
words = [w.rstrip(':') for w in text.split()]
new_dict = dict(zip(words[::2], words[1::2]))
