# How to use the hashtags on twitter using python?
hashtags = [word[1:] for word in i.text.split() if word.startswith('#')]
